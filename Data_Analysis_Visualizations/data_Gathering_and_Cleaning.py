#!/usr/bin/env python
# coding: utf-8

# # Data Gathering and Cleaning

# ## five main steps for data science processing.

# In[1]:


# 1. Data acquisition is where you read data from various sources of unstructured data, semistructured data, or full-structured data that might be stored in a spreadsheet, comma-separated file, web page, database, etc.
# 2. Data cleaning is where you remove noisy data and make operations needed to keep only the relevant data.
# 3. Exploratory analysis is where you look at your cleaned data and make statistical processing fits for specific analysis purposes.
# 4.An analysis model needs to be created. Advanced tools such as machine learning algorithms can be used in this step.
# 5.Data visualization is where the results are plotted using various systems provided by Python to help in the decision-making process.


# In[2]:


# libraries for data gathering, cleaning, integration, processing, and visualizing.


# In[3]:


# • Pandas is an open source Python library used to load, organize, manipulate, model, and analyze data by offering powerful data structures.
# • Numpy is a Python package that stands for “numerical Python. It is a library consisting of multidimensional array objects and a collection of routines for manipulating arrays. It can be used to perform mathematical, logical, and linear algebra operations on arrays.
# • SciPy is another built-in Python library for numerical integration and optimization.
# • Matplotlib is a Python library used to create 2D graphs and plots. It supports a wide variety of graphs and plots such as histograms, bar charts, power spectra, error charts, and so on, with additional formatting such as control line styles, font properties, formatting axes, and more.


# ## Cleaning Data

# In[14]:


# Creating a Data Frame Including NaN
import pandas as pd
import numpy as np
dataset = pd.DataFrame(np.random.randn(5, 3),  index=['a', 'c', 'e', 'f', 'h'],columns=['stock1','stock2', 'stock3'])
dataset.rename(columns={"one":'stock1',"two":'stock2',"three":'stock3'}, inplace=True)
dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e','f', 'g', 'h'])
print (dataset)


# In[15]:


#Checking Null Cases
print (dataset['stock1'].isnull())


# In[16]:


#Replacing NaN with a Scalar Value
import pandas as pd
import numpy as np
dataset = pd.DataFrame(np.random.randn(5, 3),  index=['a', 'c', 'e', 'f', 'h'],columns=['stock1','stock2', 'stock3'])
dataset.rename(columns={"one":'stock1',"two":'stock2',"three":'stock3'}, inplace=True)
dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e','f', 'g', 'h'])
print (dataset)
dataset.fillna(0)


# In[ ]:





# In[17]:


# Fill missing values forward
import pandas as pd
import numpy as np
dataset = pd.DataFrame(np.random.randn(5, 3),  index=['a', 'c', 'e', 'f', 'h'],columns=['stock1','stock2', 'stock3'])
dataset.rename(columns={"one":'stock1',"two":'stock2',"three":'stock3'}, inplace=True)
dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e','f', 'g', 'h'])
print (dataset)
dataset.fillna(method='pad')


# In[18]:


# Dropping All NaN Rows
import pandas as pd
import numpy as np
dataset = pd.DataFrame(np.random.randn(5, 3),  index=['a', 'c', 'e', 'f', 'h'],columns=['stock1','stock2', 'stock3'])
dataset.rename(columns={"one":'stock1',"two":'stock2',"three":'stock3'}, inplace=True)
dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e','f', 'g', 'h'])
print (dataset)
dataset.dropna()


# In[19]:


# Using the replace() Function
import pandas as pd
import numpy as np
dataset = pd.DataFrame(np.random.randn(5, 3),  index=['a', 'c', 'e', 'f', 'h'],columns=['stock1','stock2', 'stock3'])
dataset.rename(columns={"one":'stock1',"two":'stock2',"three":'stock3'}, inplace=True)
dataset = dataset.reindex(['a', 'b', 'c', 'd', 'e','f', 'g', 'h'])
print (dataset)
dataset.replace(np.nan, 0 )


# In[8]:


# Creating a Matrix of Random Values
import numpy as np
np.random.randn(5, 3)


# ## Reading and Cleaning CSV Data

# In[21]:


# Reading a CSV File and Displaying the First Five Records
import pandas as pd
sales = pd.read_csv("Sales.csv")
print ("\n\n<<<<<<< First 5 records <<<<<<<\n\n" )
print (sales.head())


# In[22]:


# Read only a few records
import pandas as pd
salesNrows = pd.read_csv("Sales.csv", nrows=4)
salesNrows


# In[23]:


# Renaming Column Labels
salesNrows.rename(columns={"ORDERNUMBER":'Order#',"QUANTITYORDERED":'Qty Ordered'}, inplace=True)
salesNrows


# In[24]:


# Finding Unique Values in Columns
print (len(salesNrows['PRICEEACH'].unique()))


# In[25]:


# Replace all values that are anomalies with NaN
import pandas as pd
sales = pd.read_csv("Sales.csv", nrows=7, na_values=["n.a.", "not avilable"])
mydata = sales.head(7)
mydata


# ## Merging and Integrating Data

# In[31]:


ls -l


# In[32]:


pip install pip-autoremove
pip-autoremove pandas -y
pip install pandas


# In[33]:


import pandas as pd

april = pd.read("April2019.csv")
august = pd.read("August2019.csv")
april.head()
august.head()


# In[ ]:


#Dropping Columns 2009, 2012, 2013, and 2014
b.drop('2014', axis=1, inplace=True)
columns = ['2013', '2012']
b.drop(columns, inplace=True, axis=1)
b.head()


# In[ ]:


# Merging Two Data Sets
mergedDataSet = a.merge(b, on="Country Name")
mergedDataSet.head()


# ## Reading Data from the JSON Format

# In[34]:


#Creating and Manipulating JSON Data
import json data = '''{
         "name" : "Ossama",
         "phone" : { "type" : "intl", "number" : "+971 50 244
         5467"},
         "email" : {"hide" : "No" }
         }'''
info = json.loads(data)
print ('Name:',info["name"])
print ('Hide:',info["email"]["hide"])


# ## Reading and Parsing an HTML File

# In[35]:


import urllib from bs4
import BeautifulSoup
response = urllib.request.urlopen('http://python-data.dr-chuck.net/known_by_Rona.html'
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
print(html_doc[:700])
print("\n")
print (soup.title)
print(soup.title.string)
print(soup.a.string)


# In[ ]:


import urllib.request
with urllib.request.urlopen("http://python-data.dr-
          chuck.net/known_by_Rona.html") as url:
                  strhtml = url.read()
          #I'm guessing this would output the html source code?
          print(strhtml[:700])


# In[ ]:




