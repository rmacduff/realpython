#!/usr/bin/env python
""" This script splits an input csv file into multiple csv files based
on the row limit split argument."""

import argparse
import csv
import os
import sys

def file_readable(input_file):
    """ Returns input_file if file exists and is readable """
    if os.path.isfile(input_file) and os.access(input_file, os.R_OK):
        return input_file
    else:
        msg = "{} does not exist or is not readable".format(input_file)
        raise argparse.ArgumentTypeError(msg)

def validate_row_limit(parser, row_limit, input_file):
    ''' Return None if row_limit is greater than the number of non-header lines
    in the csv input_file.  Set parser error message and exit otherwise. '''
    if row_limit > file_line_count(input_file) - 1:
        msg = "Row limit (-r) is greater then the number of lines in the file"
        parser.error(msg)
        sys.exit(1)

def file_line_count(filename):
    ''' Return the number of lines in filename '''
    return sum(1 for line in open(filename, 'r'))

def get_chunk_filename(filename_base, chunk):
    ''' Return chunked filename '''
    return "{}_{}.csv".format(filename_base, chunk)

def write_chunk(csv_reader, header, row_limit, chunk_num, out_file_base):
    ''' Write chunk of row_limit size from csv_reader to file named using the
     base name out_file_base. '''
    chunk = []
    for idx, line in enumerate(csv_reader):
        if idx >= row_limit:
            break
        chunk.append(line)

    out_filename = get_chunk_filename(out_file_base, chunk_num)
    with open(out_filename, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for line in chunk:
            csv_writer.writerow(line)

def write_csv_chunks(input_file, output_file_base, row_limit):
    ''' Write out input_file in row_limit sized chunks to files named using the
    base name output_file_base. '''
    with open(input_file, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        line_count = file_line_count(input_file)
        chunk_count = line_count / row_limit
        for chunk_num in xrange(chunk_count):
            write_chunk(csv_reader, header, row_limit, chunk_num, output_file_base)

def main():
    ''' Main entry point if called as an executable.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        action='store',
                        dest='input_file',
                        type=file_readable,
                        required=True,
                        help='input file name')
    parser.add_argument('-o',
                        action='store',
                        dest='output_file_base',
                        required=True,
                        help='output file name base')
    parser.add_argument('-r',
                        action='store',
                        dest='row_limit',
                        required=True,
                        type=int,
                        help='row limit to split')

    validate_row_limit(parser, parser.parse_args().row_limit, parser.parse_args().input_file)

    write_csv_chunks(parser.parse_args().input_file,
                     parser.parse_args().output_file_base,
                     parser.parse_args().row_limit)


if __name__ == '__main__':
    main()
