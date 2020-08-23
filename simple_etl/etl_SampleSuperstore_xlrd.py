# -*- coding: utf-8 -*-
"""
Created on 8/20/2020
@author: Anthony Hamlin
Program: etl_SampleSuperstore_xlrd.py
This program is a simple ETL -- extract, transform and load.
"""
import xlrd
book = xlrd.open_workbook('datasets/SampleSuperstore.xls')

# how many sheets are in the xls document
print("Number of sheets in this document are {}.".format(book.nsheets))
# Name of the sheets
print("The name of each sheet in this document are {}.".format(book.sheet_names()))
# hold sheet names
our_sheet_names = book.sheet_names()

print()  # provide space in output
# access a sheet by name
sheet_three = book.sheet_by_name("People")
# return sheet_three row data by using the sheet name
print('==== Sheet by Name: ' + our_sheet_names[2] + ' ====')  # provide space in output
for r in range(sheet_three.nrows):
    print(sheet_three.row(r))

print()  # provide space in output
# access a sheet by index
sheet_3 = book.sheet_by_index(2)
# return sheet_three row data by using the sheet index
print('==== Sheet by index: ' + our_sheet_names[2] + ' ====')  # provide space in output
# return sheet_3 row data
for i in range(sheet_3.nrows):
    print(sheet_3.row(i))
