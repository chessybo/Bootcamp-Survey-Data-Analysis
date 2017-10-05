# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:32:52 2017

@author: cches
"""

import numpy as np
import pandas as pd

data_file2 = pd.read_csv('Coders_Part_2.csv', dtype={'attended_event_types': object})
attended_event = data_file2['attended_event_types']

datatest = np.array(['haven\'t', 'not', 'none', 'never', 'havent', 'nothing', 'None', 'Not', 'Never', 'Nothing', 'Havent', 'Haven\'t', 'no', 'nope', 'No', 'Nope', 'none.', 'None.', 'haven\'t.', 'not.', 'never.', 'havent.', 'nothing.', 'Not.', 'Never.', 'Nothing.', 'Havent.', 'Haven\'t.', 'no.', 'nope.', 'No.', 'Nope.'])
# find a better way to vary between Capitals and periods.
test = pd.Series(datatest)
mask = np.in1d(attended_event, test)

new_list = [i for i in mask if i==True]
print(new_list)
print(sum(1 if x==True else 0 for x in mask))
