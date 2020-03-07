#!/usr/bin/env python
# encoding: utf-8
from googletrans import Translator
import re


class Translate:
    def __init__(self):
        self.trans_content = []
        self.not_trans_dic = ['>', '#', '!', '$']
        self.re_pattern = re.compile(r'([a-zA-Z]\.\d{1,2})|([a-zA-Z]\d{1,2}[,.])|(\d{1,2}[-–]\d{1,2})')

    def translate(self, content):
        translator = Translator(service_urls=['translate.google.cn'])
        for line in content:
            if not line:
                self.trans_content.append(line.strip('\n') + '  \n')
            else:
                self.trans_content.append(line)
            if len(line) > 6 and line[0] not in self.not_trans_dic:
                line = re.sub(self.re_pattern, fix_citation_num, line)
                # line = re.sub(r'((\d{1,2})(,|(\.)))|(((\d{1,2})[-–](\d{1,2}))(,|(\.)))', '.', line)
                translation = translator.translate(line.strip(), dest='zh-cn').text
                self.trans_content.append(translation + '\n\n')


def fix_citation_num(temp):
    if temp.group()[0].isalpha():
        if temp.group()[1] == '.':
            return temp.group()[0] + '. [' + temp.group()[2:] + '].'
        else:
            return temp.group()[0] + '. [' + temp.group()[1:] + '].'
    else:
        return '. [' + temp.group() + '].'
