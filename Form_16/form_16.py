#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 8/13/2020
Purpose: Form 16 password protect
"""


import PyPDF2
import os
import argparse
import glob
import re
import pandas as pd


def set_password(input_file, user_pass, out_name, out_path):
    """
    Function creates new pdf file with same content,
    assigns given password to pdf.
    """
    # temporary output file with name same as input file but prepended
    # by "temp_", inside same direcory as input file.
    #path, filename = os.path.split(input_file)
    output_file = os.path.join(out_path, out_name)

    output = PyPDF2.PdfFileWriter()

    input_stream = PyPDF2.PdfFileReader(open(input_file, "rb"))

    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))

    outputStream = open(output_file, "wb")

    # Set user and owner password to pdf file
    output.encrypt(user_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()

    # Rename temporary output file with original filename, this
    # will automatically delete temporary file
    #os.rename(output_file, input_file)


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--input_pdf', required=True,
    #                     help='Input pdf file')
    # parser.add_argument('-p', '--user_password', required=True,
    #                     help='output CSV file')
    # parser.add_argument('-o', '--owner_password', default=None,
    #                     help='Owner Password')
    # args = parser.parse_args()
    # ['/Users/jarvis/Downloads/Form_16/ABHIJEET SINGH SHEKHAWAT/GBCPS2003G_2020-21.pdf',
    # '/Users/jarvis/Downloads/Form_16/ABHIJEET SINGH SHEKHAWAT/GBCPS2003G_PARTB_2020-21.pdf']
    base_dir = '/Users/jarvis/Downloads/Latest Pending Forms 2/'
    input_dir = '/Users/jarvis/Downloads/Pending Form-16 Both Parts 2/'
    files = glob.glob(input_dir+"/**/*.pdf", recursive=True)
    # files = glob.glob(input_dir+"/PIYUSH GUPTA/*.pdf", recursive=True)
    print(len(files))
    string='('
    not_changed=[]
    files_db = pd.DataFrame(files)
    files_db.to_csv('files.csv', index=False)
    for file in files:
        if file.find(string) != -1:
            # print(file.find(string))
            not_changed.append(file)
            # print(file)
        else:
            try:
                name_key = r'\/([\w\s\(\)]+)\/[\w\d\s\-]+.pdf$'
                name = re.findall(name_key, file)[0]
                # print(name)
                out_path = base_dir+name+'/'
                # print(out_path)
            except:
                not_changed.append(file)
                continue
            try:
                file_key = r'\/([a-zA-Z0-9]+)[\w\d\-]+.pdf$'
                pan = re.findall(file_key, file)[0]
                # print(pan)
            except:
                not_changed.append(file)
                continue
            try:
                part_key = r'\/[a-zA-Z0-9]+[_]+([\D]+)[\d-]+.pdf$'
                # print(re.findall(part_key, file))
                if len(re.findall(part_key, file)) == 0:
                    part = 'PARTA'
                else:
                    part = 'PARTB'
                # print(part)
            except:
                not_changed.append(file)
                continue
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            out_name = name+'_'+part+'.pdf'
            set_password(file, pan, out_name, out_path)
    not_changed_db = pd.DataFrame(not_changed)
    not_changed_db.to_csv('not_changed.csv', index=False)

if __name__ == "__main__":
    main()
