"""
Takes a pdf file prints out the text of it
"""

import pdfplumber
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='pdf file to extract text from', required=True)
    args = parser.parse_args()
    pdf_file = args.file
    if not os.path.exists(pdf_file):
        print('File does not exist')
        sys.exit(1)
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            print(page.extract_text())

if __name__ == '__main__':
    main()
