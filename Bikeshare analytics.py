
# coding: utf-8

# In[21]:

import pandas
q1_bikeshare = pandas.read_csv("2015-Q1-Trips-History-Data.csv")
q1_bikeshare.columns.values


# In[20]:

time_length_sec = q1_bikeshare['Total duration (ms)']*0.001
sum(time_length_sec<60)

