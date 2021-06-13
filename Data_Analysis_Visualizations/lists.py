#!/usr/bin/env python
# coding: utf-8

# # Data Collection Structures

# ## Lists :

# In[1]:


#A list is a sequence of values of any data type that can be accessed forward or backward. Each value is called an element or a list item. 


# In[5]:


List1 = [1,2,3,4,5,6,7,8,9]
print(List1)


# In[3]:


colors = ['red','green','orange','blue']
print(colors)


# In[4]:


nested = [1,4,6,[4,67,54],34,23]
print(nested)


# ## Accesing lists

# In[6]:


print(List1[2])


# In[7]:


print(List1[2:])


# In[8]:


print(List1[:2])


# In[10]:


print(List1[-2])


# ## Adding and Updating Lists

# In[11]:


#Adding and Updating Lists


# In[12]:


print(colors)


# In[13]:


colors.append('violet')
print(colors)


# In[14]:


colors[2] = 'pink'


# In[15]:


print(colors)


# In[16]:


print(colors[:])


# ## Deleting an Element from a List

# In[17]:


print(List1[:])


# In[18]:


del List1[6]
print(List1[:])


# In[19]:


List1.remove(4) #remove does not work on the index but actual element
print(List1[:])


# In[20]:


List1.remove(2) 
print(List1[:])


# ## Basic List Operations

# In[21]:


print (len([5, "Omar", 3]))


# In[22]:


print ([3, 4, 1] + ["Omar", 5, 6]) #concartenate


# In[23]:


print (['Eg!'] * 4) #repeat element 


# In[24]:


list1 = ['Egypt', 'chemistry', 2017, 2018]
list2 = [1, 2, 3, [4, 5]]
list3 = ["a", 3.7, '330', "Omar"]

print (list1[2]) #print 3rd element
print (list2 [3:])#print all after 3rd element
print (list3 [-3:-1])#print from 3rd last to 1st
print (list3[-3])


# In[25]:


seq=(41, 12, 9, 74, 3, 15) # use sequence for creating a list


# In[26]:


tickets=list(seq)


# In[27]:


print (tickets)


# In[28]:


tickets.sort()
print (tickets)


# In[29]:


Word = 'Egypt'
List1 = list(Word)
print (List1)


# In[30]:


Greeting= 'Welcome-to-Egypt'
List2 =Greeting.split("-")
print (List2)
         


# In[31]:


Greeting= 'Welcome-to-Egypt'
delimiter='-'
List2 =Greeting.split(delimiter)
print (List2)


# In[32]:


list_demo = open('list_demo.txt')
for line in list_demo:
    line = line.rstrip()
    List = line.split()
    print(List)


# In[34]:


list_demo = open('list_demo.txt')
for line in list_demo:
    print(line)


# ## Dictionaries

# In[36]:


# You can create a dictionary and assign a key-value pair directly. In addition, you can create an empty dictionary and then assign values to each generated key


# In[37]:


Prices = {"Honda":40000, "Suzuki":50000,
"Mercedes":85000, "Nissan":35000, "Mitsubishi": 43000}
print (Prices)


# In[38]:


STDMarks = dict()
STDMarks['Salwa Ahmed']=50
STDMarks['Abdullah Mohamed']=80
STDMarks['Sultan Ghanim']=90
print (STDMarks)
         


# ## Updating and Accessing Values in Dictionaries

# In[39]:


STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80,"Sultan Ghanim":90}
STDMarks['Salwa Ahmed'] = 85 # update current value of the key 'Salwa Ahmed'
STDMarks['Omar Majid'] = 74 # Add a new item to the dictionary
print (STDMarks)


# ## Accessing Dictionary Elements

# In[44]:


Staff_Salary = { 'Omar Ahmed' : 30000 , 'Ali Ziad' :
24000, 'Ossama Hashim': 25000, 'Majid Hatem':10000}
print('Salary package for Ossama Hashim is ', Staff_Salary['Ossama Hashim'])


# ## Deleting Dictionary Elements
#         
#         
#         

# In[56]:


STDMarks={"Salwa Ahmed":50, "Abdullah Mohamed":80,"Sultan Ghanim":90}
print (STDMarks)
         
del STDMarks['Abdullah Mohamed'] # remove entry with key 'Abdullah Mohamed'
print (STDMarks)
STDMarks.clear() # remove all entries in STDMarks dictionary
print (STDMarks)


# In[ ]:




