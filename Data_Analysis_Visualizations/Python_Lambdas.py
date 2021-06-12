#!/usr/bin/env python
# coding: utf-8

# # Python_Lambdas

# In[26]:


# The lambda operator is a way to create small anonymous functions
# Lambda functions are used in combination with the functions filter(), map(), and reduce(). 
#Anonymous functions refer to functions that aren’t named and are created by using the keyword lambda. 
#A lambda is created without using the def keyword; it takes any number of arguments and returns an evaluated expression


# ## Anonymous Function Definition

# In[27]:



summation=lambda val1, val2: val1 + val2#Call summation as a function
print ("The summation of 7 + 10 = ", summation(7,10) )


# In[28]:


result = lambda x, y : x * y
result(2,5)


# ## The map() Function

# In[29]:


#The map() function is used to apply a specific function on a sequence of data. The map() function has two arguments.
#r = map(func, seq)


# In[30]:


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
Temp = (15.8, 25, 30.5,25)
F = list ( map(fahrenheit, Temp))
C = list ( map(celsius, F))
print ("Fahrenheit of (15.8, 25, 30.5,25) is: " ,  F)
print ("Celsius of ", F, " is: ", C)


# In[31]:


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
for x in Fahrenheit:
    print(x)


# ## The filter() Function

# In[32]:


# The filter() function is an elegant way to filter out all elements of a list for which the applied function returns true.


# In[33]:


fib = [0,1,1,2,3,5,8,13,21,34,55,78,56,55]
result = filter(lambda x: x % 2==0, fib)
for x in result:
    print(x)


# ## The reduce () Function

# In[34]:


# The reduce() function continually applies the function func to a sequence seq and returns a single value.


# In[35]:


import functools

f = lambda a,b: a if (a > b) else b #iterate and return the greatest number
functools.reduce(f, [47,11,42,102,13])


# In[36]:


functools.reduce(lambda x,y: x+y, [47,11,42,13])

