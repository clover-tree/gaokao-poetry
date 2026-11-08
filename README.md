# 高考必背 60 篇

本项目包含高考语文必背的 60 篇古诗文，并另收高中语文统编教材要求背诵的 21 篇（见 `textbook.json`），整理为 JSON 格式，便于程序化处理和学习。

## 文件结构

- `poetry.json`：包含所有 60 篇古诗文的完整内容，每篇文章以 JSON 对象存储，字段包括标题、作者和内容。每篇文章以 `title`（标题）、`author`（作者）和 `content`（内容）字段存储。
- `sentences.json`：将文章拆分为句子形式，便于逐句学习和分析。每篇文章以 `title`（标题）、`author`（作者）和 `content`（句子数组）字段存储。
- `textbook.json`：高中语文统编教材要求背诵的 21 篇，格式与 `sentences.json` 相同，按「每条 1–3 个分句」排布，详见[课本要求的背诵篇目](#课本要求的背诵篇目)。
- `hitokoto.js`：一个简单的 JavaScript 模块，可供处理 `sentences.json` 文件中的句子，实现 Hitokoto 风格的随机句子输出。
- `example.html`：包含一个简单的网页，展示 `hitokoto.js` 模块的使用方法。可以直接[在浏览器中打开](https://clover-yan.github.io/gaokao-poetry/example.html)查看效果。
- `utils` 文件夹：包含一些实用的 Python 脚本，用于处理 JSON 文件。
  - `divide.py`：将 `sentences.json` 文件中的内容拆分并存储为 `divided.json` 文件。
  - `split.py`：将一段原文按句末标点拆分为句子数组，用于新增篇目，用法见[用脚本新增篇目](#用脚本新增篇目)。
- `generated` 文件夹：包含一些自动生成的文件。
  - `divided.json`：由 `divide.py` 自动生成。内容和格式与 `sentences.json` 相同，但将每句单独存储在单个 JSON 对象中，便于随机抽取。每个句子以 `title`（标题）、`author`（作者）和 `content`（句子数组，仅含有一个句子）字段存储。  
    **注：出于兼容 `hitokoto.js` 模块的考虑，`content` 字段仍然是一个数组。**

## 注意

- 本项目基于[半生瓜「高考必背 60 篇」项目](https://wwz.lanzouj.com/b02jeq7sh)（密码 `f5bk`）整理，非常感谢。
- 本项目通过转换器将 `高考古诗文汇编 文字版 20231021.pdf` 文件转换为 TXT 文本，然后通过 Python 脚本将其转换为 JSON 格式，仅经过生僻字码位对齐等有限人工核查，**错误在所难免，在使用时请务必注意校对**！
- 本项目由 PDF 文件转化而来，原始文件排版混乱，经过重新排版后，缩进、换行全部丢失。因此，**本项目中古文不分段、词不分上下片**，请谅解。
- 本项目中拆句版本系通过 Python 脚本根据标点符号自动化拆分，经过部分人工修改，修改了部分特别短的句子。由于古文的特点，部分句子长度过大在所难免，请谅解。
  - **特别注意**：
    - 《〈论语〉十二章》在 `sentences.json` 中共有 13 个条目，因为《颜渊》的内容较长，拆分为 2 个条目。
    - 《赤壁赋》中，由于对话内容断句需要，移除了 `客曰：`、`苏子曰：` 字样；
    - 《种树郭橐驼传》中，由于对话内容断句需要，移除了 `有问之，对曰：`、`驼曰：` 字样。

    **如需使用完整古诗文，请务必使用 `poetry.json` 文件，而不是用 `sentences.json` 文件拼接！**
- 本项目中含有部分生僻字，如 `𫐓`、`𪭢`、`𪩘` 等。如出现显示问题，推荐安装使用[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)系列免费字体。
## 内容示例

### poetry.json
```json
[
	{
		"title": "劝学",
		"author": "《荀子》",
		"content": "君子曰：学不可以已。青，取之于蓝，而青于蓝；冰，水为之，而寒于水。木直中绳，𫐓以为轮，其曲中规。虽有槁暴，不复挺者，𫐓使之然也。故木受绳则直，金就砺则利，君子博学而日省乎己，则知明而行无过矣。吾尝终日而思矣，不如须臾之所学也；吾尝跂而望矣，不如登高之博见也。登高而招，臂非加长也，而见者远；顺风而呼，声非加疾也，而闻者彰。假舆马者，非利足也，而致千里；假舟楫者，非能水也，而绝江河。君子生非异也，善假于物也。积土成山，风雨兴焉；积水成渊，蛟龙生焉；积善成德，而神明自得，圣心备焉。故不积跬步，无以至千里；不积小流，无以成江海。骐骥一跃，不能十步；驽马十驾，功在不舍。锲而舍之，朽木不折；锲而不舍，金石可镂。蚓无爪牙之利，筋骨之强，上食埃土，下饮黄泉，用心一也。蟹六跪而二螯，非蛇鳝之穴无可寄托者，用心躁也。"
	}, ...
]
```

### sentences.json
```json
[
	{
		"title": "劝学",
		"author": "《荀子》",
		"content": [
			"君子曰：学不可以已。",
			"青，取之于蓝，而青于蓝；冰，水为之，而寒于水。",
			"木直中绳，𫐓以为轮，其曲中规。",
			"虽有槁暴，不复挺者，𫐓使之然也。", ...
		]
	}, ...
]
```

### divided.json
```json
[
	{
		"title": "劝学",
		"author": "《荀子》",
		"content": [
			"君子曰：学不可以已。"
		]
	}, ...
]
```

## 课本要求的背诵篇目

`textbook.json` 收录高中语文统编教材要求背诵的 21 篇，格式与 `sentences.json` 相同，可直接配合 `hitokoto.js` 使用：

> 《短歌行》《沁园春·长沙》《梦游天姥吟留别》《登高》《念奴娇·赤壁怀古》《劝学》《师说》《赤壁赋》《子路、曾皙、冉有、公西华侍坐》《阿房宫赋》《六国论》《〈论语〉十二章》《大学之道》《〈老子〉四章》《屈原列传》《过秦论》《离骚》（节选）《蜀道难》《蜀相》《陈情表》《兰亭集序》

分句说明：

- 每条为 1–3 个分句（分句以 `，`、`；`、`。`、`！`、`？` 结尾），多数为 2 个，即上下句；拆行处保留原标点，因此部分条目会以「，」结尾。
- 需要拆开的对话/引文去掉外层引号，保留「子曰：」「对曰：」「古人云：」等提示语。
- 与「60 篇」重叠的 17 篇也按上述规则重新切分，不再沿用 `sentences.json` 的分句。
- 按教材要求只收指定部分的篇目：《师说》仅收第一段，《屈原列传》仅收第三段，《离骚》（节选）仅收第 3 段，《过秦论》收上篇全文。
- 《过秦论》为便于分行，删去了两处人名列举长句：「齐明、周最、陈轸、召滑、楼缓、翟景、苏厉、乐毅之徒通其意，」「吴起、孙膑、带佗、倪良、王廖、田忌、廉颇、赵奢之伦制其兵。」。
- 《〈老子〉四章》在每章末尾保留教材的章次标注（如「（第十一章）」），与《〈论语〉十二章》保留出处标注的做法一致。

### textbook.json
```json
[
	{
		"title": "沁园春·长沙",
		"author": "毛泽东",
		"content": [
			"独立寒秋，湘江北去，橘子洲头。",
			"看万山红遍，层林尽染；",
			"漫江碧透，百舸争流。", ...
		]
	}, ...
]
```

### 用脚本新增篇目

`utils/split.py` 可以把一段原文自动分句，结果可直接写进 `textbook.json`（或其它同格式文件）：

```bash
# 1. 把原文（UTF-8）存成 txt
# 2. 只预览分句结果（输出句子数组）
python utils/split.py 原文.txt

# 3. 生成一个完整的条目 JSON
python utils/split.py 原文.txt -t 篇名 -a 作者 -o 条目.json

# 4. 或直接追加到 textbook.json（按原格式写回）
python utils/split.py 原文.txt -t 篇名 -a 作者 --append textbook.json

# 5. 按 textbook.json 的排版规则切分（1–3 个分句一条，多为上下句）
python utils/split.py --clauses 原文.txt
```

默认按句末标点（`。`、`！`、`？`）切句，短于 8 字的句子并入相邻较短的一侧；加 `--clauses` 则按 `textbook.json` 的规则切成分句组，并去掉拆开处的外层引号。`python utils/split.py -h` 查看全部参数。

脚本只做机械切分，原项目中人工调整过的断句与删节（如《过秦论》删去的人名长句）不会被自动复现，用完仍建议人工过一遍。

## 贡献

欢迎提交议题或拉取请求，帮助改进本项目。

## 联系

如有问题或建议，请[联系 Clover Yan](https://www.khyan.top/contact)。

## 版权

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/clover-yan/gaokao-poetry">gaokao-poetry</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.khyan.top">Clover Yan</a> is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

- 本项目仅供学习和研究使用，所有古诗文均为公共领域作品。这意味着，使用本项目中的内容本身时，无需遵循任何版权限制。
- 诗文内容参考了[半生瓜「高考必背 60 篇」项目](https://wwz.lanzouj.com/b02jeq7sh)（密码 `f5bk`），再次感谢。
- 本项目中的代码和 JSON 文件均在 CC BY-SA 4.0 许可证下发布。这意味着，直接使用本项目中的代码和 JSON 文件时，您需要遵循 CC BY-SA 4.0 许可证的条款和条件。  
  简单来说：您可以自由使用、修改和分发本项目中的代码和 JSON 文件，但必须在相同的许可证下共享您的修改版本，并且必须给出适当的署名。
