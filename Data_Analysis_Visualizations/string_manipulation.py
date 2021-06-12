#!/usr/bin/env python
# coding: utf-8

# # String Manipulation

# ## String loops

# In[2]:


fruit ='banana'
index=0
while index< len(fruit):
    letter = fruit [index]
    print (index, letter)
    index=index+1


# ## String Slicing

# In[3]:


s="Welcome to Higher Colleges of Technology"
print (s[0:4]) #first 4 letters
print (s[6:7]) #starting from 6th to 7th 
print (s[6:20]) #starting from 6th to 20th
print (s[:12]) #first 12 letters
print (s[2:]) #all after 2nd letter
print (s [:]) #everyting 
print (s)     #everything


# ## String conversion

# In[4]:


str3 = '123'
str3= int (str3)+1
print (str3)


# ## String functions and methods

# In[13]:


var1 =' Higher Colleges of Technology '
var2='College'
var3='g'
print (var1.upper())  #capitalize
print (var1.lower())  #to lower case
print (len(var1)) #length of string
print (var1.count(var3) ) # find how many g letters in var1
print (var1.endswith(' '))
print (var1.startswith('O'))
print (var1.find('h', 0, 29))
print (var1.lstrip()) # It removes all leading whitespace of a string in var1
print (var1.rstrip()) # It removes all trailingwhitespace of a string in var1
print (var1.strip()) # It removes all leading andtrailing whitespace
print ('\n') #empty line
print (var1.replace('Colleges', 'University')) #replaces the word


# ## Parsing and Extracting strings

# In[15]:


Maindata = 'From ossama.embarak@hct.ac.ae Sunday Jan 4 09:30:50 2017' 
atpost = Maindata.find('@') #first occurence of @
print ("\n<<<<<<<<<<<<<<>>>>>>>>>>>>>")
print (atpost)#firt 19 chracters
print (Maindata[ :atpost]) #create and print array of first 19
data = Maindata[ :atpost]
name=data.split(' ')
print (name)
print (name[1].replace('.', ' ').upper())
print ("\n<<<<<<<<<<<<<<>>>>>>>>>>>>>")

