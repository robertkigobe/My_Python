#!/usr/bin/env python
# coding: utf-8

# # Python Interview

# ## Robert Kigobe

# In[104]:


#There are multiple rooms
#Each room is composed of regions indexed in matrix fashion depending on their location in the room by i,j = 1...L_x, 1….L_y
#Each region has a set of trays indexed in matrix fashion m,n == 1...lx 1….ly
#Two sensors are assigned to each tray:
#I: those that output ['A', 'B', 'C', 'D'] states for each tray
#II: those that output a continuous number from 0 to 100
#tray are of multiple kinds 'S-1' to 'S-N' N = 100
#each sensor reading has a specific datetime assigned to it


# In[2]:


#Create rooms
import pandas as pd
import numpy as np
rooms =  pd.Series(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10'])
rooms


# In[3]:


#Create Regions

tray = np.arange(1, 26).reshape(5,5)
# print out regions 
for i in range(5): 
    for j in range(5): 
        print("R",tray[i][j], end = " ") 
    print() 


# In[4]:



#Create trays
tray = np.arange(1, 17).reshape(4,4)
# print out trays 
for i in range(4): 
    for j in range(4): 
        print("S",tray[i][j], end = " ") 
    print() 


# In[5]:


#create functions to generate random values for any day in the month of june for sensor 1 and sensor 2

import random
import time

startDate = "6/1/2021 1:00 AM"
endDate = "6/30/2021 11:59 PM"
    
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
    


# In[87]:


#Necessary imports
import pandas as pd
import numpy as np
import string
import random

string.ascii_letters='ABCD'
random.choice(string.ascii_letters)
random_number = random.randint(1, 100)

#Create rooms
rooms =  pd.Series(['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10'])


for Room, value in rooms.items():
    print(">>>>>>=====New Room ======<<<<<")
    
    region = np.arange(1, 26).reshape(5,5)
    # Assign regions to rooms
    
    for i in range(5): 
        for j in range(5): 
            

            #Declare a null combined Dataframe to store all sensor1 data
            sensor1Dfcombined = pd.DataFrame({'Date': pd.Series([], dtype='datetime64[ns]'),'Status': pd.Series([], dtype='str') })
           
        #Declare a null combined Dataframe to store all sensor2 data
            sensor2Dfcombined = pd.DataFrame({'Date': pd.Series([], dtype='datetime64[ns]'),'Amount': pd.Series([], dtype='int') })
           
        #Assign trays to regions
            tray = np.arange(1, 17).reshape(4,4)
            
            for k in range(4): 
                for l in range(4): 
                    
                        
                        
                    print(f"\nRoom : {value}")
                    print("Region R",region[i][j]) 
                    print("Tray S",tray[k][l]) 
                    #Generate dummy sensor data
                    sensor1 = [[random_date(startDate, endDate, random.random()),random.choice(string.ascii_letters)],[random_date(startDate, endDate, random.random()),random.choice(string.ascii_letters)],[random_date(startDate, endDate, random.random()),random.choice(string.ascii_letters)],[random_date(startDate, endDate, random.random()),random.choice(string.ascii_letters)]]
                    sensor1Df = pd.DataFrame(sensor1, columns=['Date', 'Status'])
                    print("===Sensor 1 Data ====")
                    print(sensor1Df)
                    
                    #Append all sensor1Data to process for average
                    sensor1Dfcombined = sensor1Dfcombined.append(sensor1Df)
                        
                    
                    sensor2 = [[random_date(startDate, endDate, random.random()),random.randint(1, 100)],
                       [random_date(startDate, endDate, random.random()),random.randint(1, 100)],
                       [random_date(startDate, endDate, random.random()),random.randint(1, 100)],
                       [random_date(startDate, endDate, random.random()),random.randint(1, 100)]]
                    sensor2Df = pd.DataFrame(sensor2, columns=['Date', 'Amount'])
                    print("\n===Sensor 2 Data ===\n")
                    print(sensor2Df)
                #find out what the average of each sensor II readings are for each component of type N<20 in room F10
                if value == 'F10':
                   
                         sensor2Dfcombined = sensor2Dfcombined.append(sensor2Df)
                
                        
                    
                print() 
        print() 


# In[62]:


#Explore combined data
sensor2Dfcombined.head()


# In[67]:


# find out what the average of each sensor II readings are for each component of type N<20 in room F10
sensor2Df20 = sensor2Dfcombined[sensor2Dfcombined['Amount'] <=20]
sensor2Df20.head
sensor2Df20['Amount'].mean()


# In[88]:


#find out on average how many components have sensor reading of state 'B' in a room
sensor1Dfcombined.head()


# In[89]:


sensor1Dfcombined['Status'].describe()

(sensor1Dfcombined.groupby('Status').size()/sensor1Dfcombined['Status'].count())*100


# In[97]:


#plot daily average 3 for the last 30 days

import matplotlib.pyplot as plt
plt.scatter(sensor2Dfcombined['Amount'], sensor2Dfcombined['Date'])
plt.figure(figsize=(12, 12))
plt.show()


# In[103]:


# You have two two sets of data points one is a list of tuples with a sensor_reading V and timestamp T and the other one is a list of tuples with a position of mobile sensor X and timestamp T. We want to plot the spatial interpolated map of sensor values V(X) - how do we do that?

#interp2d requires the one-dimensional arrays, so we convert reading v and reading x into 1D by matching the dates
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 13)
v = np.array([0, 2, 3, 3.5, 3.75, 3.875, 3.9375, 4])
X, V = np.meshgrid(x, v)
Z = np.sin(np.pi*X/2) * np.exp(V/2)

x2 = np.linspace(0, 4, 65)
v2 = np.linspace(0, 4, 65)
f = interp2d(x, v, Z, kind='cubic')
Z2 = f(x2, v2)

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].pcolormesh(X, V, Z)

X2, V2 = np.meshgrid(x2, v2)
ax[1].pcolormesh(X2, V2, Z2)

plt.show()


# In[ ]:




