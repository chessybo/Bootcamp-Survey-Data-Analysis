# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:47:54 2017

@author: cches
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file = pd.read_csv('FCC_New_Coders_Survey_Data.csv', dtype={'AttendedBootcamp': float, 'CodeEventOther': object, 'JobRoleInterestOther': object})
AttendedBootcamp = data_file['AttendedBootcamp']
BootcampFullJobAfter = data_file['BootcampFullJobAfter']
BootcampRecommend = data_file['BootcampRecommend']
Age = data_file['Age']

JobYes = data_file[data_file.BootcampFullJobAfter == 1]
JobNo = data_file[data_file.BootcampFullJobAfter == 0]
RecYes = data_file[data_file.BootcampRecommend == 1]
RecNo = data_file[data_file.BootcampRecommend == 0]
"""is there a way to combine attributes using the variable names?"""
RecYesJobYes = data_file[data_file.BootcampRecommend == 1][data_file.BootcampFullJobAfter == 1 ]
RecNoJobYes = data_file[data_file.BootcampRecommend == 0][data_file.BootcampFullJobAfter == 1 ]
RecYesJobNo = data_file[data_file.BootcampRecommend == 1][data_file.BootcampFullJobAfter == 0 ]
RecNoJobNo = data_file[data_file.BootcampRecommend == 0][data_file.BootcampFullJobAfter == 0 ]



"""Age Sentiment Analysis"""
y1 = [len(RecYes[RecYes.Age == i]) - len(RecNo[RecNo.Age == i]) for i in range(16, 60)]
y2 = [len(RecYesJobYes[RecYesJobYes.Age == i]) - len(RecNoJobYes[RecNoJobYes.Age == i]) for i in range(16, 60)]
y3 = [len(RecYesJobNo[RecYesJobNo.Age == i]) - len(RecNoJobNo[RecNoJobNo.Age == i]) for i in range(16, 60)]


x = range(16, 60) 
fig = plt.figure(figsize=(8,8))
plt.plot(x, y1, label = 'all')
plt.plot(x, y2, label = 'job afterwards')
plt.plot(x, y3, label = 'no job afterwards')
plt.xlabel('Age')
plt.ylabel('Net reccomendation (count)')
plt.title('Age Sentiment')
plt.xticks(x)
plt.xscale('linear')
ax = fig.add_subplot(1, 1, 1)         
ax.xaxis.set_ticks(np.arange(15, 65, 5))
plt.xlabel('Age', horizontalalignment='center', verticalalignment='center')
plt.legend()
plt.show()
