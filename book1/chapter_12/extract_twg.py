#!/usr/bin/env python
''' For exercises on page 144 in chapter 12 of book 1 of Real Python. '''

import os
from pyPdf import PdfFileReader, PdfFileWriter

PDF_INPUT_FILE_NAME = 'The Whistling Gypsy.pdf'
TXT_OUTPUT_FILE_NAME = 'The Whistling Gypsy.txt'
PDF_OUTPUT_FILE_NAME = 'The Whistling Gypsy - no_cover.pdf'
PDF_OUTPUT_DIR_NAME = 'output'

def display_pdf_info(pdf_input_file):
    ''' Prints title, author and number of pages of pdf_input_file.'''

    title = pdf_input_file.getDocumentInfo().title
    author = pdf_input_file.getDocumentInfo().author
    num_pages = pdf_input_file.getNumPages()
    print "PDF Title: {}".format(title)
    print "PDF Author: {}".format(author)
    print "Number of pages: {}".format(num_pages)

def extract_pdf_to_txt(pdf_input_file_reader, txt_output_file):
    ''' Extract the contents of pdf_input_file_reader as txt and output into
    txt_output_file. '''

    with open(txt_output_file, 'wb+') as out_file:
        for page in extract_pdf_pages(pdf_input_file_reader, 0):
            out_file.write(page)

def copy_pdf_no_cover(pdf_input_file_reader, pdf_output_file):
    ''' Make a copy of pdf_input_file_reader at pdf_output_file but
    without the first/title page. '''

    output_pdf = PdfFileWriter()
    for page in extract_pdf_pages(pdf_input_file_reader, 1, out_fmt='pdf'):
        output_pdf.addPage(page)

    output_file = open(pdf_output_file, 'wb+')
    output_pdf.write(output_file)
    output_file.close()

def extract_pdf_pages(pdf_file_reader, start_page=0, out_fmt='txt'):
    ''' A generator that yields pages from pdf_file_reader.  Start from
    start_page, and select the output format with out_fmt. '''

    for page_num in range(start_page, pdf_file_reader.getNumPages()):
        if out_fmt == 'txt':
            page = pdf_file_reader.getPage(page_num).extractText()
            page = page.replace("  ", "\n")
            page = page.encode('utf-8')
        elif out_fmt == 'pdf':
            page = pdf_file_reader.getPage(page_num)
        else:
            raise ValueError("Unkown value for out_fmt: {}".format(out_fmt))

        yield page


def main():
    ''' The main event. '''

    working_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_output_dir = os.path.join(working_dir, PDF_OUTPUT_DIR_NAME)
    pdf_input_file = os.path.join(working_dir, PDF_INPUT_FILE_NAME)
    txt_output_file = os.path.join(working_dir, TXT_OUTPUT_FILE_NAME)
    pdf_output_file = os.path.join(pdf_output_dir, PDF_OUTPUT_FILE_NAME)

    # Interesting discussion on creating directories:
    # http://stackoverflow.com/a/273227
    if not os.path.exists(pdf_output_dir):
        os.makedirs(pdf_output_dir)

    pdf_input_file_reader = PdfFileReader(file(pdf_input_file, 'rb'))

    display_pdf_info(pdf_input_file_reader)
    extract_pdf_to_txt(pdf_input_file_reader, txt_output_file)
    copy_pdf_no_cover(pdf_input_file_reader, pdf_output_file)

if __name__ == '__main__':
    main()
