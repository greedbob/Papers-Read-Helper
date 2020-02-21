#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup

from .read_pdf import ReadPdf
from .get_soup import GetSoup
from .read_html import ReadHtml
from .translate import Translate


class Paper2Markdown:
    def __init__(self):
        self.mod = 0  # 0: 'url', 1: '.html file, 2: '.pdf file''
        self.is_trans = False
        self.db = ''  # wiley, rsc
        self.url = ''
        self.src_file = ''
        self.md_file = ''
        self.trans_md_file = ''

        self.get_soup = GetSoup()
        self.read_html = ReadHtml()
        self.read_pdf = ReadPdf()
        self.translate = Translate()

        self.article_part = BeautifulSoup(features='html.parser')
        self.content = []
        self.trans_content = []
        self.md = ''

    def paper2markdown(self, src, db, is_trans=False):
        self.db = db
        if not src or not db:
            print('Error: wrong args.')
            raise ValueError
        elif src[-3:] == 'pdf':
            self.mod = 2
            self.src_file = src
        elif src[:4] == 'http':
            self.mod = 0
            self.url = src
            if 'html' not in src:
                self.src_file = src.split('/')[-1] + '.html'
            else:
                self.src_file = src.split('/')[-1]
        elif src[-4:] == 'html':
            self.mod = 1
            self.src_file = src
        else:
            raise ValueError
        self.md_file = self.src_file + '.md'
        self.trans_md_file = self.src_file + '.trans.md'
        self.read_article()
        if is_trans:
            self.is_trans = True
            self.translate.translate(self.content)
            self.trans_content = self.translate.trans_content
        self.write_md_to_file()

    def read_article(self):
        if self.mod == 2:
            self.read_pdf.read(self.src_file)
            self.content = self.read_pdf.content
        else:
            self.get_soup.get(mod=self.mod, src_file=self.src_file, url=self.url, db=self.db)
            self.article_part = self.get_soup.article_part
            self.read_html.read(self.article_part, self.db)
            self.content = self.read_html.content

    def print_article(self):
        for line in self.content:
            print(line, end='')

    def print_translate_article(self):
        for line in self.trans_content:
            print(line, end='')

    def write_md_to_file(self):
        with open(self.md_file, "w", encoding='utf-8') as md_file:
            for line in self.content:
                md_file.write(line)
        if self.is_trans:
            self.print_translate_article()
            with open(self.trans_md_file, "w", encoding='utf-8') as trans_md_file:
                for line in self.trans_content:
                    trans_md_file.write(line)
        else:
            self.print_article()


if __name__ == '__main__':
    paper2md = Paper2Markdown()
