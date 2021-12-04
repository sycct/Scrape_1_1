#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import requests
from io import StringIO
import csv
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from urllib.request import urlopen
from io import open, BytesIO
from zipfile import ZipFile
from bs4 import BeautifulSoup


class ProcessCSVPDFDOCX(object):
    def __init__(self):
        self._csv_path = 'https://image.pdflibr.com/crawler/blog/country.CSV'
        self._session = requests.Session()
        self._pdf_path = 'https://image.pdflibr.com/crawler/blog/markdown-cheatsheet-online.pdf'
        self._docx_path = 'https://image.pdflibr.com/crawler/blog/test_document.docx'

    def read_csv(self):
        response = self._session.get(self._csv_path)
        # 将文本设置成 utf-8 的编码方式
        response.encoding = 'utf-8'
        response_text = response.text
        data_file = StringIO(response_text)
        dict_reader = csv.DictReader(data_file)

        print(dict_reader.fieldnames)

        for row in dict_reader:
            print(row)

    def read_pdf(self, pdf_file):
        rscmgr = PDFResourceManager()
        retstr = StringIO()
        laparames = LAParams()
        device = TextConverter(rscmgr, retstr, laparams=laparames)
        process_pdf(rscmgr, device, pdf_file)
        device.close()

        content = retstr.getvalue()
        retstr.close()
        return content

    def read_pdf_main(self):
        pdf_file = urlopen(self._pdf_path)
        # 通过 open 打开 PDF 文件
        # pdf_file = open("../files/text.pdf", 'rb')
        output_string = self.read_pdf(pdf_file)
        print(output_string)
        pdf_file.close()

    def convert_docx_to_xml(self):
        word_file = urlopen(self._docx_path).read()
        word_file = BytesIO(word_file)
        document = ZipFile(word_file)
        xml_content = document.read('word/document.xml')

        word_obj = BeautifulSoup(xml_content.decode('utf-8'), features="html.parser")
        text_string = word_obj.findAll("w:t")
        for text_ele in text_string:
            print(text_ele.text)


if __name__ == '__main__':
    ProcessCSVPDFDOCX().convert_docx_to_xml()
