#!/usr/bin/env python
# coding: utf-8

# # CSC 732 Pattern Recognition and Neural Networks
# Instructor: Dr. Natacha Gueorguieva
# 
# Contributors:
# 
# Robert Kigobe,
# Aayushi Chirag Thakkar,
# Nikitha Pulluri
# 
# Date: 09-september-2021
# 
# QN: Part 1

# In[1]:


# increase width of jupyter notebook cells
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[2]:


# pandas is an open source,  high-performance library with , easy-to-use data structures and data analysis tools for the Python programming language.
import pandas as pd 
from pandas.plotting import scatter_matrix

# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
import matplotlib.pyplot as plt

#sklearn Built on NumPy, SciPy, and matplotlib also used for data analysis
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
import seaborn as sns

#numpy used to manipulate numerical data in python
import numpy as np


# # Import and explore dataset
# ## read_csv() pandas function 

# In[3]:


#Import the dataset
dataset = pd.read_csv ('seeds_dataset.csv', header=None) 


# ## set up column names

# In[4]:


#Setup the column names
dataset.columns= ['area','perimeter','compactness', 'kernel length',   'kernel width',  'asymmetry coefficient', 'kernel groove Length']
print (dataset)


# In[5]:


# Print shape of dataset
print(dataset.shape)


# In[6]:


# Peak at first 20 lines of dataset
print(dataset.head(20))


# ## Generate descriptive statistics can be achieved with dataset.describe()

# Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.Analyzes both numeric and object series, as well as DataFrame column sets of mixed data types. The output will vary depending on what is provided.

# In[7]:



print(dataset.describe())


# In[8]:


# Print class distribution of dataset
print(dataset.groupby('area').size())


# # Visualize dataset
# 
# ## Box or whisker Plots
# 

# A Box Plot is also known as Whisker plot is created to display the summary of the set of data values having properties like minimum, first quartile, median, third quartile and maximum. In the box plot, a box is created from the first quartile to the third quartile, a vertical line is also there which goes through the box at the median. Here x-axis denotes the data to be plotted while the y-axis shows the frequency distribution.

# In[9]:



dataset.plot(kind='box', subplots=True, layout=(7,5), sharex=False, sharey=False, figsize=(20,30))
plt.show()


# According to the box plots, it can be seen that the kernel groove length has the median far away from the true middle of the box which could indicate that the data is skewed for the column.

# In[10]:


# histograms
dataset.hist(figsize=(10,10))
plt.show()


# considering the assymentry coefficient, compactness, we see that the the histograms are bell shaped incating that the data is uni modal.thus a good sign of good data distribution.
# 
# considering area,perimeter,kernel length and kernel width, the histograms are Right-Skewed. this is an indication that this is a unimodal data set, with the mode closer to the left of the graph and smaller than either the mean or the median. This also indicated that the mean is located to the right side of the graph and will be a greater value than either the median or the mode. This shape indicates that there are a number of data points, perhaps outliers, that are greater than the mode.
# 
# The kernel groove length has two bell shapes indicating bi-modal behavior

# ## scatter plot matrix

# In[11]:



scatter_matrix(dataset, figsize=(10,10))
plt.show()


# there is a good concentration of the data on the regression line indicationg that most of the data is rightly placed. the outliers can also be seemainly in the assymetry coeficcient and the kernel groove length.

# In[ ]:




