#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup


class ReadHtml:
    def __init__(self):
        self.article_part = BeautifulSoup(features='html.parser')
        self.content = []

    def read(self, soup, db):
        self.article_part = soup
        if db == 'wiley':
            self.read_wiley()
        elif db == 'rsc':
            self.read_rsc()
        else:
            raise TypeError

    def read_wiley(self):
        for part in self.article_part:
            if 'class' in part.attrs:
                if 'article-section__abstract' in part.attrs['class']:
                    self.content.append('### {}\n'.format(part.find('h2').string))
                    for string in part.find('p').strings:
                        self.content.append(string)
                elif 'article-section__full' in part.attrs['class']:
                    pass
                elif 'article-section__content' in part.attrs['class']:
                    for child in part.children:
                        if child.name == 'h2':
                            self.content.append('\n### {}\n'.format(child.string))
                        elif child.name == 'p':
                            for string in child.strings:
                                self.content.append(string.strip())
                            self.content.append('\n')
                        elif child.name == 'section':
                            temp = child.select("figure > a")
                            self.content.append('![]({})\n\n'.format(temp[0].attrs['href']))

    def read_rsc(self):
        for part in self.article_part:
            if part.name == 'div' and part.attrs['class'][0] == 'article__title':
                self.content.append('## {}\n\n'.format(part.get_text().strip()))
            elif part.name == 'div' and part.attrs['class'][0] == 'article__authors':
                author_line = '> '
                for author in part:
                    if author.name == 'span' and author.attrs['class'][0] == 'article__author-link':
                        author_line += author.a.string.replace('\n', ' ') + ', '
                self.content.append(author_line)
                self.content.append('\n\n')
            elif part.name == 'h3':
                self.content.append('### {}\n'.format(part.get_text().strip()))
            elif part.name == 'div' and part.attrs['class'][0] == 'capsule__column-wrapper':
                self.content.append('{}\n\n'.format(part.get_text().strip()))
            elif part.name == 'div' and part.attrs['class'][0] == 't-html':
                for para in part:
                    if para.name == 'h2':
                        self.content.append('### {}\n\n'.format(para.get_text().strip()))
                    elif para.name == 'p':
                        self.content.append('{}\n\n'.format(para.get_text().strip()))
                    elif para.name == 'div' and para.attrs['class'][0] == 'img-tbl':
                        fig = para.select('figure > a')
                        self.content.append('![{0}]({1})  \n'.format(fig[0].attrs['name'], fig[0].attrs['href']))
                        self.content.append('{}\n\n'.format(para.find_all('span')[1].get_text().strip()))
