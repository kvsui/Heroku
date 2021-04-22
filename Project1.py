#!/usr/bin/env python
# coding: utf-8

# In[59]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticks


# In[3]:


power = pd.read_csv("file_02.csv")
states = pd.read_csv("State_region_corrected.csv")


# In[4]:


power


# In[5]:


power = power.drop(['index'],axis=1)


# In[6]:


power.shape


# In[7]:


states


# In[8]:


power['Date']=pd.to_datetime(power['Date'])


# In[9]:


power.dtypes


# In[10]:


power['Thermal Generation Actual (in MU)']=power['Thermal Generation Actual (in MU)'].replace(',','', regex=True).astype(float)
power['Thermal Generation Estimated (in MU)']=power['Thermal Generation Estimated (in MU)'].replace(',','', regex=True).astype(float)


# In[11]:


power.isna().any()


# In[12]:


power['Region'].value_counts()


# In[13]:


grpbyreg = power.groupby('Region')
l = []
ind = []
for index, group in grpbyreg:
    ind.append(index)
    l.append(group)
ser = pd.Series(l,index=ind)        


# In[14]:


ser['Eastern']['Nuclear Generation Actual (in MU)'].fillna(0,inplace = True)
ser['Eastern']['Nuclear Generation Estimated (in MU)'].fillna(0,inplace = True)
ser['Eastern']  


# In[15]:


ser['NorthEastern']['Nuclear Generation Actual (in MU)'].isnull().sum()
ser['NorthEastern']['Nuclear Generation Actual (in MU)'].fillna(0,inplace = True)
ser['NorthEastern']['Nuclear Generation Estimated (in MU)'].fillna(0,inplace = True)
ser['NorthEastern']


# In[16]:


finaldf = pd.concat([ser['Eastern'],ser['NorthEastern'],ser['Western'],ser['Northern'],ser['Southern']])
finaldf=finaldf.reset_index()


# In[17]:


finaldf.drop('index',axis=1,inplace=True)


# In[18]:


finaldf


# In[173]:


group1 = finaldf.groupby([finaldf['Date'].dt.year,'Region'])
series_thermal= group1['Thermal Generation Actual (in MU)'].agg(np.sum)
fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(15,15))

series_thermal[2017].plot(kind= "bar",ax=axes[0,0],title = "Thermal Generation in 2017")
series_thermal[2018].plot(kind= "bar",ax=axes[0,1],title = "Thermal Generation in 2018")
series_thermal[2019].plot(kind= "bar",ax=axes[1,0],title = "Thermal Generation in 2019")
series_thermal[2020].plot(kind= "bar",ax=axes[1,1],title = "Thermal Generation in 2020")
fig.tight_layout(pad = 3.0)
plt.savefig("TG")


# In[175]:


series_hydro= group1['Hydro Generation Actual (in MU)'].agg(np.sum)
fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(15,15))

series_hydro[2017].plot(kind= "bar",ax=axes[0,0],title = "Hydro Generation in 2017")
series_hydro[2018].plot(kind= "bar",ax=axes[0,1],title = "Hydro Generation in 2018")
series_hydro[2019].plot(kind= "bar",ax=axes[1,0],title = "Hydro Generation in 2019")
series_hydro[2020].plot(kind= "bar",ax=axes[1,1],title = "Hydro Generation in 2020")
fig.tight_layout(pad = 3.0)
plt.savefig("HG")


# In[176]:


series_nuclear= group1['Nuclear Generation Actual (in MU)'].agg(np.sum)
fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(15,15))

series_nuclear[2017].plot(kind= "bar",ax=axes[0,0],title = "Nuclear Generation in 2017")
series_nuclear[2018].plot(kind= "bar",ax=axes[0,1],title = "Nuclear Generation in 2018")
series_nuclear[2019].plot(kind= "bar",ax=axes[1,0],title = "Nuclear Generation in 2019")
series_nuclear[2020].plot(kind= "bar",ax=axes[1,1],title = "Nuclear Generation in 2020")
fig.tight_layout(pad = 3.0)
plt.savefig("NG")


# In[177]:


group2 = finaldf.groupby(finaldf['Date'].dt.year)
explode=(0,0.1,0.2)
fig = plt.figure(figsize=(18,10))
ax1 = plt.subplot2grid((2,2),(0,0))
plt.pie(group2.agg(np.sum).loc[2017,['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)']],labels=['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)'],explode=explode,colors=["g","r","b"],autopct="%1.1f%%")
plt.title('2017 Distribution')
ax1 = plt.subplot2grid((2,2),(0,1))
plt.pie(group2.agg(np.sum).loc[2018,['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)']],labels=['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)'],explode=explode,colors=["g","r","b"],autopct="%1.1f%%")
plt.title('2018 Distribution')
ax1 = plt.subplot2grid((2,2),(1,0))
plt.pie(group2.agg(np.sum).loc[2019,['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)']],labels=['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)'],explode=explode,colors=["g","r","b"],autopct="%1.1f%%")
plt.title('2019 Distribution')
ax1 = plt.subplot2grid((2,2),(1,1))
plt.pie(group2.agg(np.sum).loc[2020,['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)']],labels=['Thermal Generation Actual (in MU)','Nuclear Generation Actual (in MU)','Hydro Generation Actual (in MU)'],explode=explode,colors=["g","r","b"],autopct="%1.1f%%")
plt.title('2020 Distribution')
plt.savefig("Pie")



# # Hypothesis 
# 
# Energy consumed by any state ∝ Area

# # State wise Analysis

# In[42]:


df2 = group2.agg(np.sum)
s=[]
for i in range(2017,2021):
    s.append(df2.loc[i])
Total_Energy_2017=s[0].agg(np.sum)
Total_Energy_2018=s[1].agg(np.sum)
Total_Energy_2019=s[2].agg(np.sum)
Total_Energy_2020=s[3].agg(np.sum)


# In[179]:


fig1 = plt.figure(figsize=(20,20))
ax1 = plt.subplot2grid((2,2),(0,0))
axs1=plt.bar(states['State / Union territory (UT)'],states['National Share (%)']*Total_Energy_2017)
plt.xticks(rotation='vertical')
plt.title("2017")
ax1 = plt.subplot2grid((2,2),(0,1))
axs1=plt.bar(states['State / Union territory (UT)'],states['National Share (%)']*Total_Energy_2018)
plt.xticks(rotation='vertical')
plt.title("2018")
ax1 = plt.subplot2grid((2,2),(1,0))
axs1=plt.bar(states['State / Union territory (UT)'],states['National Share (%)']*Total_Energy_2019)
plt.xticks(rotation='vertical')
plt.title("2019")
ax1 = plt.subplot2grid((2,2),(1,1))
axs1=plt.bar(states['State / Union territory (UT)'],states['National Share (%)']*Total_Energy_2020)
plt.xticks(rotation='vertical')
fig1.tight_layout(pad=3.0)
plt.title("2020")
plt.savefig("state")


# # Comparison between Estimates and Actual Production

# In[155]:


labels=s[0][1:6:2].index
x = np.arange(len(labels))
width = 0.35
fig2,ax=plt.subplots()
rects1=ax.bar(x-width/2,s[0][0:6:2].values,width,label="Actual")
rects2=ax.bar(x+width/2,s[0][1:6:2].values,width,label="Estimated")
ax.set_ylabel('Units in MU')
ax.set_title("Comparison between Actual and Estimates in 2017")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
for tick in ax.get_xticklabels():
    tick.set_rotation(90)


# In[158]:


labels=s[1][1:6:2].index
x = np.arange(len(labels))
width = 0.35
fig2,ax=plt.subplots()
rects1=ax.bar(x-width/2,s[1][0:6:2].values,width,label="Actual")
rects2=ax.bar(x+width/2,s[1][1:6:2].values,width,label="Estimated")
ax.set_ylabel('Units in MU')
ax.set_title("Comparison between Actual and Estimates in 2018")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
for tick in ax.get_xticklabels():
    tick.set_rotation(90)


# In[161]:


labels=s[2][1:6:2].index
x = np.arange(len(labels))
width = 0.35
fig2,ax=plt.subplots()
rects1=ax.bar(x-width/2,s[2][0:6:2].values,width,label="Actual")
rects2=ax.bar(x+width/2,s[2][1:6:2].values,width,label="Estimated")
ax.set_ylabel('Units in MU')
ax.set_title("Comparison between Actual and Estimates in 2018")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
for tick in ax.get_xticklabels():
    tick.set_rotation(90)


# In[162]:


labels=s[3][1:6:2].index
x = np.arange(len(labels))
width = 0.35
fig2,ax=plt.subplots()
rects1=ax.bar(x-width/2,s[3][0:6:2].values,width,label="Actual")
rects2=ax.bar(x+width/2,s[3][1:6:2].values,width,label="Estimated")
ax.set_ylabel('Units in MU')
ax.set_title("Comparison between Actual and Estimates in 2018")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
for tick in ax.get_xticklabels():
    tick.set_rotation(90)


# In[ ]:




