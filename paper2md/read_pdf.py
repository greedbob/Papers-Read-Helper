#!/usr/bin/env python
# encoding: utf-8
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.converter import PDFPageAggregator


class ReadPdf:
    def __init__(self):
        self.content = []

    def read(self, src):
        with open(src, 'rb') as file:
            parser = PDFParser(file)
            doc = PDFDocument(parser)
            rsc_mgr = PDFResourceManager()
            device = PDFPageAggregator(rsc_mgr, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsc_mgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for part in layout:
                    page_content = ''
                    if isinstance(part, LTTextBoxHorizontal):
                        results = part.get_text()
                        part_content = results.replace("\n", '').replace(u'\u3000', u'')
                        if part_content != '' and len(part_content) > 2:
                            page_content += part_content
                            page_content += '\n\n'
                            self.content.append(page_content)
