#!/usr/bin/env python
# coding: utf-8

# # Tabular Data and Data Formats

# In[1]:


# create a data frame using the counstructor pandas.DataFrame( data, index, columns, dtype, copy)


# In[2]:


#Pandas does the following
#Provides a mechanism to load data objects from different formats
#Creates efficient data frame objects with default and customized indexing
#Reshapes and pivots date sets
#Provides efficient mechanisms to handle missing data 
#Merges, groups by, aggregates, and transforms data
#Manipulates large data sets by implementing various functionalities such as slicing, indexing, subsetting, deletion, and insertion
#Provides efficient time series functionality


# ## Pandas Series

# In[3]:


# A series is a one-dimensional labeled array 


# In[4]:


import pandas as pd #imports pandas library
import numpy as np #imports numpy library
data = np.array([90,75,50,66]) #creates an array 
s = pd.Series(data,index=['A','B','C','D']) #assigns labels to the array
print (s)


# In[5]:


data = {'Ahmed' : 92, 'Ali' : 55, 'Omar' : 83}
s = pd.Series(data,index=['Ali','Ahmed','Omar'])
print (s)


# ## Pandas Data Frame

# In[6]:


# A data frame is a two-dimensional data structure


# In[7]:


import pandas as pd
data = [['Robert',42],['Ahmed',35],['Ali',17],['Omar',25]]
DataFrame1 = pd.DataFrame(data,columns=['Name','Age'])
print (DataFrame1)


# In[8]:


DataFrame1[1:] #retrieve data from a data frame starting from index 1 up to the end of rows.


# In[9]:


#create a data frame using a dictionary.


# In[10]:


import pandas as pd
data = {'Name':['Robert','Ahmed', 'Ali', 'Omar','Salwa'],'Age':[42,35,17,25,30]}
dataframe2 = pd.DataFrame(data, index=[100, 101, 102, 103,104]) 
print (dataframe2)


# In[16]:


pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]))

