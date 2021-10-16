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
# QN: Part 3

# Seaborn is a library mostly used for statistical plotting in Python. It is built on top of Matplotlib and provides beautiful default styles and color palettes to make statistical plots more attractive.

# In[1]:


# increase width of jupyter notebook cells
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# # Load Data
# 
# sns not able to load a non demo dataset so we shall use pandas to load the seeds dataset as before

# In[2]:


# Load Libraries
import seaborn as sns
import numpy as np
from pandas import read_csv
from pandas import set_option
import warnings
#warnings.simplefilter(action='ignore', category=FutureWarning)

warnings.filterwarnings("ignore")


# In[3]:


#Import the dataset
dataset = read_csv ('seeds_dataset.csv', header=None) 
#Setup the column names

names= ['area','perimeter','compactness', 'kernel length',   'kernel width',  'asymmetry coefficient', 'kernel groove Length']
dataset.columns = names
dataset


# # Desity Plots

# In[4]:


#plot the distribution of the DataFrame "Profit" column
#set the style we wish to use for our plots
sns.set_style("darkgrid")
sns.distplot(dataset['compactness'])


# In[5]:


sns.distplot(dataset['area'])


# In[7]:


# univariate box and whisker plots done using seaborn
import matplotlib.pyplot as plt
plt.figure(figsize=(30,20))
for i,column in enumerate(dataset.columns):
    try:
        plt.subplot(7,5,1+i)
        sns.boxplot(data=dataset[column], orient='v')
        plt.ylabel(column)
    except:
        pass


# # Joint plots

# In[8]:


sns.jointplot(x='compactness',y='area',data=dataset, kind='reg')


# In[9]:


sns.jointplot(x='compactness',y='kernel length',data=dataset, kind='hex')


# # Pairplot

# In[10]:


sns.pairplot(dataset,hue='area')


# In[11]:


# scatter plot matrix
sns.pairplot(dataset, hue='area', diag_kind='hist')
plt.show()


# In[12]:


sns.pairplot(dataset,hue='asymmetry coefficient',palette='magma')


# In[13]:


# histograms
plt.figure(figsize=(20,30))
for i,column in enumerate(dataset.columns):
    try:
        plt.subplot(7,5,1+i)
        sns.distplot(dataset[column], kde=False)
    except:
        pass


# In[14]:


# plot Univariate KDE plots
plt.figure(figsize=(20,30))
for i,column in enumerate(dataset.columns):
    try:
        plt.subplot(7,5,1+i)
        sns.distplot(dataset[column])
    except:
        pass


# In[16]:


# seaborn code for part 3
plt.figure(figsize=(10,10))
corr = dataset.corr(method='pearson')
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True)


# In[17]:


# plot of hierarchically-clustered heatmap
# better correlation matrix
sns.clustermap(corr, center=0, cmap="vlag",
               linewidths=.75, figsize=(10, 10))


# In[ ]:




