#!/usr/bin/env python
# encoding: utf-8
from googletrans import Translator
import re


class Translate:
    def __init__(self):
        self.trans_content = []
        self.not_trans_dic = ['>', '#', '!', '$']

    def translate(self, content):
        translator = Translator(service_urls=['translate.google.cn'])
        for line in content:
            if not line:
                self.trans_content.append(line.strip('\n') + '  \n')
            else:
                self.trans_content.append(line)
            if len(line) > 6 and line[0] not in self.not_trans_dic:
                line = re.sub(r'((\d{1,2})(,|(\.)))|(((\d{1,2})[-–](\d{1,2}))(,|(\.)))', '.', line)
                translation = translator.translate(line.strip(), dest='zh-cn').text
                self.trans_content.append(translation + '\n\n')
