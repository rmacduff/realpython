#!/usr/bin/env python

import os
from pyPdf import PdfFileReader, PdfFileWriter

def display_pdf_info(pdf_input_file):
    ''' Prints title, author and number of pages of
    pdf_input_file.'''
    title = pdf_input_file.getDocumentInfo().title
    author = pdf_input_file.getDocumentInfo().author
    num_pages = pdf_input_file.getNumPages()
    print "PDF Title: {}".format(title)
    print "PDF Author: {}".format(author)
    print "Number of pages: {}".format(num_pages)

def extract_pdf_contents(pdf_input_file, txt_output_file):
    with open(txt_output_file, 'wb+') as out_file:
        for page_num in range(0, pdf_input_file.getNumPages()):
            page = pdf_input_file.getPage(page_num).extractText()
            page = page.replace("  ", "\n")
            page = page.encode('utf-8')
            out_file.write(page)

def main():
    path="/Users/ross/projects/realpython/book1/chapter_12"
    file_name="The Whistling Gypsy.pdf"
    txt_output_file="The Whistling Gypsy.txt"
    input_file_name = os.path.join(path, file_name)
    input_pdf = PdfFileReader(file(input_file_name, 'rb'))
    output_pdf = PdfFileWriter()

    display_pdf_info(input_pdf)
    extract_pdf_contents(input_pdf, txt_output_file)

if __name__ == '__main__':
    main()
