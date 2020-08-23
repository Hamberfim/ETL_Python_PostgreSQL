# -*- coding: utf-8 -*-
"""
Created on 8/20/2020
@author: Anthony Hamlin
Program: etl_SampleSuperstore_pd.py
This program is a simple ETL -- extract, transform and load.
"""
import pandas as pd

# read in each sheets data from the xls doc
orders_sheet1 = pd.read_excel('datasets/SampleSuperstore.xls', sheet_name='Orders')
returns_sheet2 = pd.read_excel('datasets/SampleSuperstore.xls', sheet_name='Returns')
people_sheet3 = pd.read_excel('datasets/SampleSuperstore.xls', sheet_name='People')

# ===== PEOPLE SHEET =====
# list the columns of a sheet
people_sheet3_col = list(people_sheet3.columns)
print("Column Titles: " + str(people_sheet3_col))
# get a shape of a sheet
people_sheet3_shape = people_sheet3.shape
print("Shape of the sheet(rows/columns): " + str(people_sheet3_shape))
print()  # space in output
# create a dataframe of some of the rows from the read in sheet data
df_head_people = people_sheet3.head(2)  # return first number of rows
print(df_head_people)
print()  # space in output
df_tail_people = people_sheet3.tail(2)  # return last number of rows
print(df_tail_people)
print()  # space in output
# all rows
df_all_people = people_sheet3
print(df_all_people)
print()  # space in output

# ===== RETURNS SHEET =====
returns_col = list(returns_sheet2.columns)
print("Returns Sheet Column Titles: " + str(returns_col))

# dataframe of returns sheet
df_returns = returns_sheet2.head(10)  # return first number of rows
print(df_returns)
print()  # space in output

# ===== ORDERS SHEET =====
orders_col = list(orders_sheet1)
print("Orders Sheet Column Titles: " + str(orders_col))

# dataframe of orders sheet
df_orders = orders_sheet1.head(5)  # return first number of rows
print(df_orders)
print()  # space in output

# glean some simple data from the orders sheet
profit_sum = orders_sheet1['Profit'].sum()
print("Sum of profit column: " + str(f"{profit_sum:.2f}"))
profit_mean = orders_sheet1['Profit'].mean()
print("Mean of profit column: " + str(f"{profit_mean:.2f}"))
