# -*- coding: utf-8 -*-
"""
Created on 8/17/2020
@author: Anthony Hamlin
Program: data_etl.py
This program is a simple ETL -- extract, transform and load.
"""
from simple_etl import dbconn
import petl as etl
import psycopg2 as pg
import csv
import sys
from sqlalchemy import *

with open('Customer_Transactions_sm.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    record_count = 1
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        print("Transaction ID: " + str(row[0])
              + ", Customer ID: " + str(row[1])
              + ", Purchase Amount: " + str(row[2])
              + ", Date of Purchase: " + str(row[3]))
        record_count += 1
print("Record #: " + str(record_count))
