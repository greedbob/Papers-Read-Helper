## Markdown-Papers-and-Translate
Assist to read and translate paper in foreign language.  
Format articles from online web pages, html files, or pdf files into markdown text, and provide cross-translation functions.  
阅读外文Paper辅助记录和翻译工具。  
将文章从在线网页版、html文件或pdf文件，格式化为markdown文本，并提供对照翻译功能。

### Contents Tree 目录结构
```
Markdown-Papers-and-Translate
┌─ .gitignore
│  README.md
│  requirements.txt
├─paper2md
│  │  paper2md.py
│  │  main.py
│  │  get_soup.py
│  │  read_html.py
│  │  read_pdf.py
│  │  translate.py
│  │  __init__.py
│  └─ __main__.py
└─test
   └─  test.py
```

### How to use? 如何使用
- 环境  
  - python3 及依赖模块`requirements.txt`  
  - `git clone https://github.com/greedbob/Markdown-Papers-and-Translate.git`
- 命令行
   - 在本仓库根目录下打开终端
   - `python`进入`python console`  
   - `from paper2md import Paper2Markdown`  
   - `paper2md.paper2markdown('rsc.html', 'rsc', is_trans=True)` # 使用测试用例的html文件，下载地址见下文
- 以脚本方式调用  
在本仓库根目录文件夹内编写py脚本`test.py`如下：  
```python
from paper2md import Paper2Markdown

paper2md = Paper2Markdown()
paper2md.paper2markdown('rsc.html', 'rsc', is_trans=True) 
# 'rsc.html' 为url或html文件或pdf文件，此处使用测试用例的html文件  
# 'rsc' 为文章所属出版社，rsc为pubs.rsc.org出版  
# is_trans 为是否翻译
# 运行后将得到rsc.html.md 和 rsc.html.trans.md，后者问中英文对照。
```

### Test 测试用例
- 首先下载[测试用html文件](https://pubs.rsc.org/en/content/articlelanding/2018/CC/C8CC01388H)
- 将html文件储存于test文件夹下，并改名为'rsc.html'
- 运行脚本

### 支持数据库
数据库 | 网址
- | -
**Royal Society of Chemistry** | https://pubs.rsc.org/
![](https://onlinelibrary.wiley.com/pb-assets/hub-assets/pericles/logo-header-1526603583437.png) | https://onlinelibrary.wiley.com/


### Contribute
- 支持更多数据库的解析
- 网页延迟加载

### LICENSE and Copyright
**MIT License**  
**Copyright (c) 2020 [@greedbob](https//blog.greedfox.me) ([Paper2Markdown](https://github.com/greedbob/Markdown-Papers-and-Translate))**
