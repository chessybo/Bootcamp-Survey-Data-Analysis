# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:59:41 2017

@author: cches
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.read_csv('FCC_New_Coders_Survey_Data.csv', dtype={'AttendedBootcamp': float, 'CodeEventOther': object, 'JobRoleInterestOther': object})
AttendedBootcamp = data_file['AttendedBootcamp']
BootcampFullJob = data_file['BootcampFullJobAfter']
BootcampRecommend = data_file['BootcampRecommend']
BootcampLoan = data_file['BootcampLoanYesNo']
BootcampName = data_file['BootcampName']
FinanciallySupporting = data_file['FinanciallySupporting']
HasChildren = data_file['HasChildren']
HasDebt = data_file['HasDebt']
FinancialDependents = data_file['HasFinancialDependents']
EmploymentStatus = data_file['EmploymentStatus']
EmploymentStatusOther = data_file['EmploymentStatusOther']
BootcampFinish = data_file['BootcampFinish']
Age = data_file['Age']
NetworkID = data_file['NetworkID']


AttendYes = data_file[data_file.AttendedBootcamp == 1]
AgeAttend = AttendYes['Age']
FinishYes = data_file[data_file.BootcampFinish == 1]
FinishNo = data_file[data_file.BootcampFinish == 0]
JobYes = data_file[data_file.BootcampFullJobAfter == 1]
JobNo = data_file[data_file.BootcampFullJobAfter == 0]
RecYes = data_file[data_file.BootcampRecommend == 1]
RecNo = data_file[data_file.BootcampRecommend == 0]
"""is there a way to combine attributes using the variable names?"""
RecYesJobYes = data_file[data_file.BootcampRecommend == 1][data_file.BootcampFullJobAfter == 1 ]
RecNoJobYes = data_file[data_file.BootcampRecommend == 0][data_file.BootcampFullJobAfter == 1 ]
RecYesJobNo = data_file[data_file.BootcampRecommend == 1][data_file.BootcampFullJobAfter == 0 ]
RecNoJobNo = data_file[data_file.BootcampRecommend == 0][data_file.BootcampFullJobAfter == 0 ]



yvar = [len(JobYes[JobYes.Age == i]) - len(JobNo[JobNo.Age == i]) for i in range(16, 60)]
x = range(16, 60)

fig = plt.figure(figsize=(8,8))
plt.plot(x, yvar, 'go')
plt.xlabel('Age')
plt.ylabel('Net Employment Difference (count)')
plt.title('Employement Discrepencies')
plt.xticks(x)
plt.xscale('linear')
ax = fig.add_subplot(1, 1, 1)
ax.spines['bottom'].set_position('zero')
plt.vlines(x, [0], yvar)           
ax.xaxis.set_ticks(np.arange(15, 65, 5))
plt.xlabel('Age', horizontalalignment='center', verticalalignment='center', x=1.05)
plt.show()



nurator = yvar
derator = [len(JobYes[JobYes.Age == i]) + len(JobNo[JobNo.Age == i]) for i in range(16, 60)]

bananasplit = []
for b, m in zip(derator, nurator):
    try:
        bananasplit.append(int(m)/int(b))
    except ZeroDivisionError:
        bananasplit.append(int(m))
        
        
fig = plt.figure(figsize=(8,8))
plt.plot(x, bananasplit, 'go')
plt.xlabel('Age')
plt.ylabel('Net Employment Difference (count)')
plt.title('Employement Discrepencies normed')
plt.xticks(x)
plt.xscale('linear')
ax = fig.add_subplot(1, 1, 1)
ax.spines['bottom'].set_position('zero')
plt.vlines(x, [0], bananasplit)           
ax.xaxis.set_ticks(np.arange(15, 65, 5))
plt.xlabel('Age', horizontalalignment='center', verticalalignment='center', x=1.05)
plt.show()








plt.figure(figsize=(8,8))
plt.title('bootcamp job')
plt.hist([JobYes['Age'], JobNo['Age']], histtype='bar', bins = 45, range=[16,61], label=['Job after camp', 'no job after camp'])
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.show()


numjobfin2 = [len(JobNo[JobNo.Age == i]) for i in range(16, 61)]
numjobfin1 = [len(JobYes[JobYes.Age == i]) for i in range(16, 61)]
demjobfin = [len(JobYes[FinishYes.Age == i]) + len(JobNo[JobNo.Age == i]) for i in range(16, 61)]

Yesjonfin =[int(m) / int(b) if int(b) != 0 else int(m) for b,m in zip(demjobfin, numjobfin1)]
Nojobfin = [int(m) / int(b) if int(b) != 0 else int(m) for b,m in zip(demjobfin, numjobfin2)]

plt.figure(figsize=(8,8))
plt.title('bootcamp job normed')
plt.xlabel('Age')
plt.ylabel('Count normed')
plt.bar(np.arange(16, 61, 1), Yesjonfin, 0.35, label='job')
plt.bar(np.arange(16, 61, 1) + 0.35, Nojobfin, 0.35, label='no job')
plt.xticks(np.arange(15, 65, 5))
plt.legend()
plt.show()

