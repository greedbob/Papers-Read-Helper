#!/usr/bin/env python
# encoding: utf-8
from urllib import request
from bs4 import BeautifulSoup


class GetSoup:
    def __init__(self):
        self.mod = 0
        self.url = ''
        self.src_file = ''
        self.db = ''

        self.article_part = BeautifulSoup(features='html.parser')

    def get(self, mod=-1, src_file='', url='', db=''):
        self.mod = mod
        self.db = db
        if self.mod == 0:
            self.url = url
            self.get_html()
            self.get_article_part()
        elif self.mod == 1:
            self.src_file = src_file
            self.get_article_part()
        else:
            raise TypeError

    def get_html(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = request.Request(self.url, headers=headers)
        resp = request.urlopen(req)
        content = resp.read()
        resp.close()
        with open(self.src_file, "w+b") as html_file:
            html_file.write(content)

    def get_article_part(self):
        with open(self.src_file, encoding='utf-8', errors='ignore') as file:
            soup = BeautifulSoup(file, 'html.parser')
            if self.db == 'wiley':
                article_part = soup.find_all('section')
            elif self.db == 'rsc':
                article_part = soup.find('article')
            else:
                print('article type error')
                raise Exception
            if len(article_part) != 0:
                self.article_part = article_part
            else:
                print('can\'t find article part')
                raise Exception
