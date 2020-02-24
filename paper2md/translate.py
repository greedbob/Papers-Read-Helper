#!/usr/bin/env python
# encoding: utf-8
from googletrans import Translator


class Translate:
    def __init__(self):
        self.trans_content = []
        self.not_trans_dic = ['>', '#', '!', '$']

    def translate(self, content):
        translator = Translator(service_urls=['translate.google.cn'])
        for line in content:
            self.trans_content.append(line.strip('\n') + '  \n')
            if len(line) > 6 and line[0] not in self.not_trans_dic:
                translation = translator.translate(line.strip(), dest='zh-cn').text
                self.trans_content.append(translation + '\n\n')
