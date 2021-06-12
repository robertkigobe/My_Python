#!/usr/bin/env python
# coding: utf-8

# # Fundamentals of python Programming

# ## Selection statements

# ### if statement

# In[1]:


x = 5
if (x==5):
    print('Equal 5')
elif x>5:
    print('Greater than 5')
elif x<5:
    ('Less than 5')


# ### for loop

# In[6]:


for a in range (3,10):
    print(a)


# ### while loop

# In[8]:


ticket = 8
while ticket >3:
    print ("Your ticket number is ",ticket)
    ticket -=1


# ### Break, Continue, Pass

# In[10]:


for letter in 'python3':
    if letter == 'o':
        break
    print(letter)


# In[11]:


a =0
while a<=5:
    a=a+1
    if a%2==0:
        continue
    print(a)
print("End of Loop")


# In[14]:


for i in [1,2,3,4,5,6,7,8,9]:
    if i==3:
        pass
        print("Pass when value is ", i)
    print(i)


# ### try and except

# In[17]:


astr = 'Robert Kigobe'
errorsms=''
try:
    istr = int(astr)  #error
except:
    istr=-1
    errorsms='\Incorrect entry'
print ("First Try:",istr,errorsms)

