#!/usr/bin/env python
# coding: utf-8

# # Basic Operations

# ## Basic lines and indentation

# In[23]:


age,mark,code = 18,65,"CSC 770"


# In[24]:


print(age)
print(mark)
print(code)


# ## Multiline statements
# 

# In[25]:


Tv,Mobile,Tablet=30,45,60


# In[26]:


#the line escape us used to create multiple lines


# In[27]:


Total = Tv +Mobile + Tablet
print(Total)


# ## Read data from users

# In[ ]:


name = input("enter your name here")
age = int (input("enter your age here"))

print("\nName =", name); print("\nAge =", age)


# ## Arithmetic operations

# In[ ]:


print (13//5) #returns remainder
print(13+5)
print(13-5)
print(2*5)
print(13/5)
print(13%5)
print(2**3) #raises the power to 


# ## Relational operators

# In[ ]:


print(13<5)
print(13>5)
print(13<=5)
print(2>=5)
print(13==5)
print(13 != 5)


# ## Logical operators

# In[ ]:


x=10>5 and 4>20 #AND operator
print(x)
x=10>5 or 4>20 #OR operator
print(x)
x= not(10<4)
print(x)

