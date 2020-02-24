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
