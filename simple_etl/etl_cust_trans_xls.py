# -*- coding: utf-8 -*-
"""
Created on 8/20/2020
@author: Anthony Hamlin
Program: etl_cust_trans_xls.py
This program is a simple ETL -- extract, transform and load.
"""
import xlrd
book = xlrd.open_workbook('SampleSuperstore.xls')

# how many sheets are in the xls document
print("Number of sheets in this document are {}.".format(book.nsheets))
# Name of the sheets
print("The name of each sheet in this document are {}.".format(book.sheet_names()))
