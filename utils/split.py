"""
把整段原文拆成句子数组，结果可直接放进 poetry.json / sentences.json / textbook.json。

用法：
	python utils/split.py 原文.txt -t 篇名 -a 作者
	python utils/split.py 原文.txt -t 篇名 -a 作者 -o 新条目.json
	python utils/split.py 原文.txt -t 篇名 -a 作者 --append textbook.json
	python utils/split.py 原文.txt --clauses

默认按句末标点（。！？）切句，短于 --merge-short（默认 8 字）的句子并入相邻句中较短的一侧。
加 --clauses 则按 textbook.json 的排版规则切成 1–3 个分句（多为上下句两句）一条，
并把拆开处的外层引号去掉。
"""

import argparse
import json
import sys

END = "。！？"
SEP = "，；"
CLOSERS = "”’》）」』"
OPENERS = "（("


def split_paragraph(paragraph, merge_short=8):
	text = "".join(ch for ch in paragraph if not ch.isspace() and ch != "\u200b")
	sentences = []
	start = 0
	i = 0
	while i < len(text):
		if text[i] in END:
			j = i + 1
			while j < len(text) and text[j] in CLOSERS:
				j += 1
			sentences.append(text[start:j])
			start = j
			i = j
		else:
			i += 1
	if start < len(text):
		sentences.append(text[start:])
	if merge_short > 0:
		sentences = merge_short_sentences(sentences, merge_short)
	return sentences


def merge_short_sentences(sentences, min_len):
	sentences = list(sentences)
	while len(sentences) > 1:
		index = next((i for i, s in enumerate(sentences) if len(s) < min_len), None)
		if index is None:
			break
		if index == 0:
			target = 1
		elif index == len(sentences) - 1:
			target = index - 1
		else:
			left, right = len(sentences[index - 1]), len(sentences[index + 1])
			target = index - 1 if left <= right else index + 1
		if target < index:
			sentences[target] += sentences[index]
		else:
			sentences[target] = sentences[index] + sentences[target]
		del sentences[index]
	return sentences


def split_text(text, merge_short=8):
	sentences = []
	for paragraph in text.splitlines():
		if paragraph.strip():
			sentences.extend(split_paragraph(paragraph, merge_short))
	return sentences


def cut(text, sep_chars):
	out = []
	start = 0
	for i, ch in enumerate(text):
		if ch in sep_chars:
			out.append(text[start:i + 1])
			start = i + 1
	if start < len(text):
		out.append(text[start:])
	return [c for c in out if c]


def sizes_for(n, max_n=3):
	if n <= max_n:
		return [n]
	sizes = []
	rem = n
	while rem > max_n:
		sizes.append(2)
		rem -= 2
	sizes.append(rem)
	return sizes


def count_parts(chunk):
	return sum(1 for ch in chunk if ch in SEP or ch in END)


def balanced(text):
	return text.count("“") == text.count("”")


def split_clauses(text):
	text = "".join(ch for ch in text if not ch.isspace() and ch != "\u200b")
	chunks = []
	start = 0
	i = 0
	n = len(text)
	while i < n:
		if text[i] in END:
			j = i + 1
			while j < n and text[j] in CLOSERS:
				j += 1
			if j < n and text[j] in OPENERS:
				close = "）" if text[j] == "（" else ")"
				k = text.find(close, j + 1)
				if k != -1:
					j = k + 1
					while j < n and text[j] in CLOSERS:
						j += 1
			for seg in cut(text[start:j], "；"):
				parts = cut(seg, "，")
				index = 0
				for size in sizes_for(len(parts)):
					chunks.append("".join(parts[index:index + size]))
					index += size
			start = j
			i = j
		else:
			i += 1
	if start < n:
		for seg in cut(text[start:], "；"):
			parts = cut(seg, "，")
			index = 0
			for size in sizes_for(len(parts)):
				chunks.append("".join(parts[index:index + size]))
				index += size
	merged = []
	i = 0
	while i < len(chunks):
		cur = chunks[i]
		if (i + 1 < len(chunks) and count_parts(cur) == 1 and count_parts(chunks[i + 1]) == 1
				and balanced(cur + chunks[i + 1])):
			merged.append(cur + chunks[i + 1])
			i += 2
		else:
			merged.append(cur)
			i += 1
	return [c if balanced(c) else c.replace("“", "").replace("”", "") for c in merged]


def main():
	parser = argparse.ArgumentParser(description="把原文拆成句子数组")
	parser.add_argument("source", help="原文文件（UTF-8）")
	parser.add_argument("-t", "--title", help="篇名，输出完整条目或追加时必填")
	parser.add_argument("-a", "--author", help="作者，输出完整条目或追加时必填")
	parser.add_argument("-o", "--output", help="写成一个条目 JSON 的文件")
	parser.add_argument("--append", help="把条目追加到已有 JSON 文件")
	parser.add_argument("--merge-short", type=int, default=8, help="短句合并阈值，默认 8，0 表示不合并")
	parser.add_argument("--clauses", action="store_true", help="按 textbook.json 的规则切成 1–3 个分句一条")
	args = parser.parse_args()

	with open(args.source, encoding="utf-8-sig") as f:
		text = f.read()
	content = split_clauses(text) if args.clauses else split_text(text, args.merge_short)

	if (args.output or args.append) and not (args.title and args.author):
		parser.error("输出完整条目或追加时必须同时给出 --title 与 --author")

	if args.append:
		with open(args.append, encoding="utf-8") as f:
			data = json.load(f)
		data.append({"title": args.title, "author": args.author, "content": content})
		with open(args.append, "w", encoding="utf-8") as f:
			json.dump(data, f, ensure_ascii=False, indent="\t")
			f.write("\n")
		print("appended %d sentences to %s" % (len(content), args.append))
	elif args.output:
		with open(args.output, "w", encoding="utf-8") as f:
			json.dump([{"title": args.title, "author": args.author, "content": content}], f, ensure_ascii=False, indent="\t")
			f.write("\n")
		print("wrote %d sentences to %s" % (len(content), args.output))
	else:
		sys.stdout.reconfigure(encoding="utf-8", errors="replace")
		print(json.dumps(content, ensure_ascii=False, indent="\t"))


if __name__ == "__main__":
	main()
