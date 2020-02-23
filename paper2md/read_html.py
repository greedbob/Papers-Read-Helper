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
        elif db == 'nature':
            self.read_nature()
        else:
            raise TypeError

    def ignore_navigable(self, temp):
        return isinstance(temp, type(self.article_part))

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

    def read_nature(self):
        for part in self.article_part:
            if not isinstance(part, type(self.article_part)):
                pass
            elif part.attrs['class'][0] == 'c-article-header':
                for block in part.header:
                    if not self.ignore_navigable(block):
                        pass
                    elif block.name == 'h1':
                        self.content.append('# {}\n'.format(block.get_text()))
                    elif block.name == 'ul' and block.attrs['data-test'] == 'authors-list':
                        author_line = ''
                        for author in block:
                            if self.ignore_navigable(author):
                                author_line += author.span.a.get_text()
                                author_line += ', '
                        self.content.append('> Authors: {}  \n'.format(author_line.rstrip(', ')))
                    elif block.name == 'p':
                        info_line = ''
                        for word in block.strings:
                            info_line += word
                        self.content.append('> Info: {}\n\n'.format(info_line.replace('\n', '')))
            elif part.attrs['class'][0] == 'c-article-body':
                for block in part.find_all('section'):
                    if not self.ignore_navigable(block):
                        pass
                    elif 'Abs' in block.attrs['aria-labelledby']:
                        self.content.append('## {}\n'.format(block.div.h2.get_text()))
                        self.content.append('{}\n\n'.format(block.div.div.p.get_text()))
                    elif 'Sec' in block.attrs['aria-labelledby']:
                        self.content.append('## {}\n'.format(block.div.h2.get_text()))
                        for line in block.div.div:
                            if line.name == 'h3':
                                self.content.append('### {}\n'.format(line.get_text()))
                            elif line.name == 'p':
                                self.content.append('{}  \n'.format(line.get_text()))
                            elif line.name == 'div':
                                if 'data-test' in line.attrs and line.attrs['data-test'] == 'figure':
                                    self.content.append('{}  \n'.format(line.figure.figcaption.b.get_text()))
                                    for item in line.figure.div:
                                        if not self.ignore_navigable(item):
                                            pass
                                        elif item.attrs['class'][0] == 'c-article-section__figure-item':
                                            self.content.append('![](https:{})  \n'.format(item.a.picture.img['src']))
                                        else:
                                            self.content.append('{}  \n\n'.format(item.p.get_text()))
                                elif 'class' in line.attrs and line.attrs['class'][0] == 'c-article-equation':
                                    self.content.append('{}  \n'.format(line.get_text()))
                                elif 'data-test' in line.attrs and line.attrs['data-test'] == 'supplementary-info':
                                    for item in line:  # Extended data figures and tables
                                        if not self.ignore_navigable(item):
                                            pass
                                        elif 'id' in item.attrs and 'Fig' in item.attrs['id']:
                                            self.content.append('### {}\n'.format(item.h3.string))
                                            self.content.append('![{}](https:{})  \n'.format(item.attrs['id'],
                                                                item.h3.a['data-supp-info-image']))
                                            self.content.append('{}\n'.format(item.div.get_text()))
