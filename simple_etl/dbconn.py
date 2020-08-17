# -*- coding: utf-8 -*-
"""
Created on 8/17/2020
@author: Anthony Hamlin
Program: dbconn.py
This script creates a pg db connection.
"""
import psycopg2 as pg
conn_string = "dbname='cust_trans' user='postgres' host='127.0.0.1' passfile='.pgpass'"

try:
    conn = pg.connect(conn_string)
    print("DB Connection Successful")
except Exception as e:
    print("Connection Error: " + str(e))
