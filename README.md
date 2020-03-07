## Papers-Read-Helper
Assist to read and translate paper in foreign language.  
Format articles from online web pages, html files, or pdf files into markdown text, and provide cross-translation functions.  
阅读外文Paper辅助记录和翻译工具。  
将文章从在线网页版、html文件或pdf文件，格式化为中英文对照翻译的markdown文本。

### Files Tree
```
./Papers-Read-Helper/
┌─paper2md
│  ├─ paper2md.py
│  ├─ main.py
│  ├─ get_soup.py
│  ├─ read_html.py
│  ├─ read_pdf.py
│  ├─ translate.py
│  ├─ __init__.py
│  └─ __main__.py
├─test
│  ├─ test.py
│  └─ test.txt
├─ .gitignore
├─ LICENSE
├─ README.md
└─ requirements.txt
```

### Introduction
- 主要目的是支持文献的html内容提取和翻译，也同时支持了pdf文本提取和纯文本仅翻译功能。
- 提供四种模式：`0: url mod, 1: .html mod, 2: .pdf mod, 3: .md or .txt mod (translate only)`
  - 模式会根据输入的参数自动选择。
  - 输入url时，下载html文件，从html文件中提取内容，翻译，输出并新建文件
  - 输入html时，从html文件中提取内容，翻译，输出并新建文件
  - 输入pdf时，从pdf中提取文字信息，翻译，输出并新建文件
  - 输入为纯文本文件时，直接翻译内容，输出并新建文件
- 输入参数有`src, db='', is_trans=False, trans_only=False`，分别为输入网址或文件名，文章所在数据库（默认为空），是否翻译（默认为否），是否仅翻译（默认为否）
- 文章数据库支持陆续增加，详见`Supported Database`部分

### Supported Database
| 数据库 | 网址 |
| - | - |
| Royal Society of Chemistry | https://pubs.rsc.org/ |
| Wiley Online Library | https://onlinelibrary.wiley.com/ |
| Nature | https://www.nature.com/ |

### How to use? 
- 环境
  - python3 及依赖模块`pip install -r requirements.txt`  
  - `git clone https://github.com/greedbob/Papers-Read-Helper.git`
- 下面部分面向无经验者介绍，可以跳过直接参考`Test Example`部分
- 命令行
  - 准备好测试用的网址/html文件/txt/md文件，放在本仓库目录内。
  - 在本仓库根目录下打开终端
  - `python`进入`python console`  
  - `from paper2md import Paper2Markdown`  
  - `paper2md.paper2markdown('rsc.html', 'rsc', is_trans=True)` # 使用测试用例的html文件，下载地址见下文
- 脚本调用
在本仓库根目录文件夹内编写py脚本并执行，提供测试脚本`test.py`如下：  
```python
from paper2md import Paper2Markdown


def html_nature_example(reader):  # 模式0：通过网址获取html文件，提取信息并翻译 参数：网址，文章所在数据库，是否翻译
    reader.paper2markdown('https://www.nature.com/articles/s41586-020-1994-5', 'nature', is_trans=True)


def html_file_rsc_example(reader):  # 模式1：提取html文件中的有效信息并翻译 参数：html文件名，文章所在数据库，是否翻译
    reader.paper2markdown('rsc.html', 'rsc', is_trans=True)


def pdf_example(reader):  # 模式2：提取pdf文件中的有效信息并翻译 参数：pdf文件名，是否翻译
    reader.paper2markdown('batteries.pdf', is_trans=False)


def text_example(reader):  # 模式3：无需提取信息，直接翻译提供的纯文本（txt/md等格式） 参数：文件名，是否仅翻译
    reader.paper2markdown('test.txt', trans_only=True)


if __name__ == '__main__':
    paper2md = Paper2Markdown()
    text_example(paper2md)
```

### Test Example
- 详见`.\test\`目录
- 测试文件：
  - 测试用url：[测试用url](https://pubs.rsc.org/en/content/articlelanding/2018/CC/C8CC01388H)
  - 测试用html文件：[测试用html文件下载](https://pubs.rsc.org/en/content/articlelanding/2018/CC/C8CC01388H)
  - 测试用纯文本文件：`test.txt`
- 将测试用文件储存于test文件夹下，修改好`tset.py`
- 运行脚本


### Contribute
- 其他数据库的解析
- 需登录加载或延迟加载的html获取

| Alipay | WeChat |
| - | - |
| <img src="https://greedbob.github.io/images/alipay-600.jpg" width = "200" > | <img src="https://greedbob.github.io/images/wechat-600.png" width = "200" > |

### LICENSE and Copyright
**MIT License**  
**Copyright (c) 2020 [@greedbob](https//blog.greedfox.me) [Paper2Markdown](https://github.com/greedbob/Markdown-Papers-and-Translate)**
