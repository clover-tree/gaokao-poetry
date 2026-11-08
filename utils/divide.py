import json


def divide(sentences):
	l = []
	for i in sentences:
		for j in i.get("content"):
			l.append({
			    "title": i.get("title"),
			    "author": i.get("author"),
			    "content": [j]
			})
	return l


filename = "textbook.json"
data = json.load(open(filename, "r", encoding="utf-8"))
result = divide(data)
with open("generated/divided.json", "w", encoding="utf-8") as f:
	json.dump(result, f, ensure_ascii=False, indent='\t')
