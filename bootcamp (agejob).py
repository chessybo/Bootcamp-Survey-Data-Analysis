# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 00:36:48 2017

@author: cches
"""
import pandas as pd
import matplotlib.pyplot as plt


data_file = pd.read_csv('FCC_New_Coders_Survey_Data.csv', dtype={'AttendedBootcamp': float, 'CodeEventOther': object, 'JobRoleInterestOther': object})
AttendedBootcamp = data_file['AttendedBootcamp']
BootcampFullJobAfter = data_file['BootcampFullJobAfter']
BootcampFinish = data_file['BootcampFinish']
Age = data_file['Age']

AttendYes = data_file[data_file.AttendedBootcamp == 1]
AgeAttend = AttendYes['Age']

FinishYes = data_file[data_file.BootcampFinish == 1]
FinishNo = data_file[data_file.BootcampFinish == 0]


JobYes = data_file[data_file.BootcampFullJobAfter == 1]
JobNo = data_file[data_file.BootcampFullJobAfter == 0]
Job = JobYes['BootcampFullJobAfter']

AgeJob = JobYes['Age']

#figure = plt.figure(figsize=(8,8))
#plt.title('Age of Bootcampers')
#plt.hist([JobYes['Age'], JobNo['Age']], histtype='bar', range=[16,70], label=['Job after camp', 'no job after camp'])
#plt.xlabel('Age')
#plt.ylabel('Count')
#plt.legend()


plt.figure(figsize=(8,8))
plt.title('bootcamp job')
plt.hist([JobYes['Age'], JobNo['Age']], histtype='bar', bins = 44, range=[16,60], label=['Job after camp', 'no job after camp'])
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()

plt.figure(figsize=(8,8))
plt.title('Attend bootcamp')
plt.hist(AttendYes['Age'], histtype='bar', range=[16,60])
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()

plt.figure(figsize=(8,8))
plt.title('bootcampfinish')
plt.hist([FinishYes['Age'], FinishNo['Age']], histtype='bar', range=[16,60], label=['finished', 'didn\'t finish'])
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()

