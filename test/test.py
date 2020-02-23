from paper2md import Paper2Markdown


def html_rsc_example(reader):
    reader.paper2markdown('rsc.html', 'rsc', is_trans=True)


def url_nature_example(reader):
    reader.paper2markdown('s41586-020-1994-5.html', 'nature', is_trans=True)


if __name__ == '__main__':
    paper2md = Paper2Markdown()
    url_nature_example(paper2md)
