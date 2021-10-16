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
# QN: Part 2

# # Load Libraries

# In[1]:


from pandas import read_csv
from pandas import set_option


# ## Load Data

# In[2]:


#Import the dataset
dataset = read_csv ('seeds_dataset.csv', header=None) 
#Setup the column names

names= ['area','perimeter','compactness', 'kernel length',   'kernel width',  'asymmetry coefficient', 'kernel groove Length']
dataset.columns = names
dataset


# In[3]:


dataset.describe()


# # Pairwise Pearson correlations

# ## Method

# In[4]:


set_option('display.width', 100)
set_option('precision', 3)
correlations = dataset.corr(method='pearson')
print(correlations)


# ## Analysis

# Pearson correlation refers to the extent to which values are inter dependent. these values range between 1.0 and -1.0. 
# ,0.9 to 1 positive or negative indicates a very strong correlation.
# ,0.7 to 0.9 positive or negative indicates a strong correlation.
# ,0.5 to 0.7 positive or negative indicates a moderate correlation.
# ,0.3 to 0.5 positive or negative indicates a weak correlation.
# ,0 to 0.3 positive or negative indicates a negligible correlation.
# 
# in our dataset, it can be that asymmetry coefficient has a very weak correlation with all the other variables while prerimeter, kernel length and kernel width have very strong correlations with all the other variables.

# # Skew for each attribute

# ## method

# In[5]:


skew = dataset.skew()
print("Skew:")
print(skew)


# ## Analysis

# Skewness is a measure of asymmetry of a distribution. In a normal distribution, the mean divides the curve symmetrically into two equal parts at the median and the value of skewness is zero.
# When a distribution is asymmetrical the tail of the distribution is skewed to one side-to the right or to the left.
# When the value of the skewness is negative, the tail of the distribution is longer towards the left hand side of the curve.
# When the value of the skewness is positive, the tail of the distribution is longer towards the right hand side of the curve.
# 
# A skewness value of 0 in the output denotes a symmetrical distribution of values in the row.
# A negative skewness value in the output indicates an asymmetry in the distribution corresponding to the row and the tail is larger towards the left hand side of the distribution.
# A positive skewness value in the output indicates an asymmetry in the distribution corresponding to the row and the tail is larger towards the right hand side of the distribution.
# 
# in our dataset, it can be interpreted that compactness is skewed to the left while the other parametwers are skewed to the right.

# # Univariate Density Plot

# ## Method

# In[6]:


# useful libraries
from matplotlib import pyplot
dataset.plot(kind='density', subplots=True, layout=(4,2), sharex=False)
pyplot.show()


# ## Analysis

# A density plot is a smoothed, continuous version of a histogram estimated from the data. A continuous curve is drawn at every individual data point and all of these curves are then added together to make a single smooth density estimation. Above is the density plots for all the points of the various attributes in the dataset.

# # Correlation Matrix Plot

# In[7]:


#useful libraries
import numpy


# ## Method

# In[8]:


correlations = dataset.corr()

# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,7,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)

pyplot.show()


# ## Interpretation

# from the heatmap above, it can be seen that the asymetric coefficient is the most uncorrelated attribute to the rest followed by the compactness, hence the skew values seen earlier. the rest of the values are closely correlated.

# # Rescaling Data

# ## Method

# In[9]:


#useful libraries
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

# separate array into input and output components
#Import the dataset
dataset = read_csv ('seeds_dataset.csv', header=None) 
array_rescale = dataset.values
X = array_rescale[:,0:6]
Y = array_rescale[:,6]

scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)

# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:7,:])


# ## Interpretation

# Rescaling a vector means to add or subtract a constant and then multiply or divide by a constant and in this case to ensure al the data lies between o and 1. A print of the first 7 rows is as above

# # Standardize Data

# ## method

# In[10]:


# import useful libraries: Standardize data (0 mean, 1 stdev)

from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions

# separate array into input and output components
#Import the dataset
dataset = read_csv ('seeds_dataset.csv', header=None) 
array_standadize = dataset.values
X = array_standadize[:,0:6]
Y = array_standadize[:,6]

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:7,:])


# ## Analysis

# Standardizing a vector means subtracting a measure of location and dividing by a measure of scale. For example, if the vector contains random values with a Gaussian distribution, you might subtract the mean and divide by the standard deviation, thereby obtaining a “standard normal” random variable with mean 0 and standard deviation 1. 
# 

# # Normalize Data,

# ## method

# In[11]:


# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
from pandas import read_csv
from numpy import set_printoptions

# separate array into input and output components
#Import the dataset
dataset = read_csv ('seeds_dataset.csv', header=None) 
array_normalize = dataset.values
X = array_normalize[:,0:6]
Y = array_normalize[:,6]

scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(normalizedX[0:7,:])


# ## Interpretation

# Normalizing a vector most often means dividing by a norm of the vector. It also often refers to rescaling by the minimum and range of the vector, to make all the elements lie between 0 and 1 thus bringing all the values of numeric columns in the dataset to a common scale.

# # Binarization

# ## method

# In[12]:


# binarization
from sklearn.preprocessing import Binarizer
from pandas import read_csv
from numpy import set_printoptions

# separate array into input and output components
#Import the dataset
dataset = read_csv ('seeds_dataset.csv', header=None) 
array_binarizer = dataset.values
X = array_binarizer[:,0:6]
Y = array_binarizer[:,6]

binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(binaryX[0:7,:])


# ## analysis

# Binarize data (set feature values to 0 or 1) according to a threshold. In our dataset, this all sets the values to 1

# In[ ]:




