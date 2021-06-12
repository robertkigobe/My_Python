#!/usr/bin/env python
# coding: utf-8

# # Python Numpy Package

# In[2]:


# Numpy is a Python package that stands for “numerical Python.” It is a library consisting of multidimensional array objects and a collection of routines for processing arrays.
#The Numpy library is used to apply the following operations:
#• Operations related to linear algebra and random number generation
#• Mathematical and logical operations on arrays
#• Fourier transforms and routines for shape manipulation
#For instance, you can create arrays and perform various operations such as adding or subtracting arrays


# ## Addition and subtraction of arrays using np.add and np.subtract

# In[4]:


import numpy as np
#addition of arrays
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
np.add(a,b)


# In[5]:


#subtraction of arrays
np.subtract(a,b) #Same as a-b


# ## Data Cleaning and Manipulation Techniques

# In[ ]:


#Keeping accurate data is highly important for any data scientist. Developing an accurate model and getting accurate predictions from the applied model depend on the missing values treatment. Therefore, handling missing data is important to make models more accurate and valid.
#Numerous techniques and approaches are used to handle missing data such as the following:
#• Fill NA forward
#• Fill NA backward
#• Drop missing values
#• Replace missing (or) generic values • Replace NaN with a scalar value
#The following examples are used to handle the missing values in a tabular data set:
#In [31]: dataset.fillna(0) # Fill missing values with zero value 
#In [35]: dataset.fillna(method='pad') # Fill methods Forward
#In [35]: dataset.fillna(method=' bfill') # Fill methods Backward 
#In [37]: dataset.dropna() # remove all missing data


# ## Abstraction of the Series and Data Frame

# In[7]:


# A series is one of the main data structures in Pandas. It differs from lists and dictionaries. An easy way to visualize this is as two columns of data. The first is the special index, a lot like the dictionary keys, while the second is your actual data. 


# ### Create a series

# In[8]:


import pandas as pd
animals = ["Lion", "Tiger", "Bear"]
pd.Series(animals)


# In[9]:


marks = [95, 84, 55, 75]
pd.Series(marks)


# In[10]:


quiz1 = {"Robert":75, "Lillian": 84, "Jackie": 70}
q = pd.Series(quiz1)
q


# ### query a series using a series using iloc(index) or loc(label)

# #### loc()

# In[15]:


q.loc['Robert']


# In[16]:


q['Robert']


# #### iloc()

# In[17]:


q.iloc[2]


# In[18]:


q.iloc[2]


# ## Numpy operation on a series

# In[19]:


import pandas as pd
import numpy as np
s = pd.Series([70,90,65,25, 99])
s


# ### summation using a loop

# In[20]:


total =0
for val in s:
    total += val
print (total)


# ### Summation using Numpy (faster function)

# In[21]:


total = np.sum(s)
print (total)


# ### Alter a series to add new values

# In[22]:


s = pd.Series ([99,55,66,88])
s.loc['Robert'] = 85
s


# ### append two or more series

# In[25]:


test = [95, 84, 55, 75] #create list
marks = pd.Series(test) #create serie 1 out of list
s = pd.Series ([99,55,66,88]) #create serie 2
s.loc['Ahmed'] = 85 #add value to serie 2
NewSeries = s.append(marks) #append seri1 to serie 2
NewSeries #print final serie

