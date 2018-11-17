# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 02:29:47 2017

@author: cches
"""

import csv, sqlite3
import pandas as pd

data_file = pd.read_csv('FCC_New_Coders_Survey_Data.csv', dtype={'AttendedBootcamp': float, 'CodeEventOther': object, 'JobRoleInterestOther': object})

con = sqlite3.connect("database_survey.db")
cur=con.cursor() # Get the cursor
csv_data = csv.reader('FCC_New_Coders_Survey_Data.csv')

with open('FCC_New_Coders_Survey_Data.csv', 'r', encoding="utf8") as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['BootcampRecommend'], i['BootcampFullJobAfter']) for i in dr]
    
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS MyTable")
    cur.execute("CREATE TABLE MyTable(BootcampRecommend, BootcampFullJobAfter);") # use your column names here
    for rows in to_db:
        cur.execute('INSERT INTO MyTable VALUES(?,?)', rows)
    cur.fetchall()
    cur.execute("SELECT COUNT(BootcampRecommend), BootcampFullJobAfter FROM MyTable WHERE BootcampRecommend='1' GROUP BY BootcampFullJobAfter")
    rows = cur.fetchall()
    
    cur.execute("SELECT COUNT(*) FROM MyTable where BootcampFullJobAfter = '1'")
    rows2 = cur.fetchall()
    
    cur.execute("SELECT COUNT(BootcampRecommend), BootcampFullJobAfter FROM MyTable WHERE BootcampRecommend='0' GROUP BY BootcampFullJobAfter")
    rows3 = cur.fetchall()
    
con.commit()
con.close()    

import numpy as np
import matplotlib.pyplot as plt

values, labels = zip(*rows[0:2]) #assigns the individual elements
values3, labels3 = zip(*rows3[0:2])
"""the unpacking operator * breaks up the list of lists into just two lists so 
when the zip() function is applied, it merges the values of the first element 
in each list """
xlocs = np.array([0, 1])
plt.bar(xlocs - 0.2, values,width=0.2,color='b',align='center', label='reccomendation')
plt.bar(xlocs, values3,width=0.2,color='g',align='center', label='no reccomendation')
plt.title("Getting Job and Reccomendation")
plt.xticks(xlocs - 0.1,  ["no job", "job"])
plt.legend(loc=(1.03,0.2))
plt.show()
