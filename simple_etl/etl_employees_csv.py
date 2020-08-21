# -*- coding: utf-8 -*-
"""
Created on 8/20/2020
@author: Anthony Hamlin
Program: etl_employees_csv.py
This program is a simple ETL -- extract, transform and load.
"""
import os
import pandas as pd
# print(os.getcwd())
# used so test and see the dataset/dataframe in the IPython console variable viewer
# dir_path = os.getcwd()
# dataset = pd.read_csv(dir_path + '\simple_etl\employees_sm.csv')
dataset = pd.read_csv('employees_sm.csv')

# rename some columns
dataset.rename(columns={"Bonus %": "Bonus", "First Name": "F_Name"}, inplace=True)
dataset.sort_values('F_Name', ascending=True, inplace=True)

# gender & finance team dataframe
df_genteam = dataset[(dataset.Gender == 'Male') & (dataset.Team == 'Finance')]
print('===== Males on the finance team =====')
print(df_genteam)
print()  # space in the output
# salary and bonus qry
df_salBonusQry = dataset.query("Salary > 135000 and Bonus > 10")
print("===== Salaries greater than $135000 and Bonus' greater than $10 =====")
print(df_salBonusQry)
print()  # space in the output
# retrieve specific people
df_aaron_donna = dataset[dataset.F_Name.isin(['Aaron', 'Donna'])]
print("===== Find people named Aaron and/or Donna =====")
print(df_aaron_donna)
