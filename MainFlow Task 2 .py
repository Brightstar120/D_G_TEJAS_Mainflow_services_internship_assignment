#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('C:\\Users\\tejas\\Downloads\\01.Data Cleaning and Preprocessing.csv')


# In[3]:


type(data)


# In[4]:


data.info #concise summary


# In[5]:


data.describe() #descriptive statistics


# In[23]:


data=data.drop_duplicates() #filtering
data


# In[25]:


data.isnull()


# In[26]:


data.isnull().sum()


# In[27]:


data.notnull()


# In[28]:


data.isnull().sum().sum()


# In[29]:


data2=data.fillna(value=0)
data2


# In[30]:


data3=data.fillna(method='pad')
data3


# In[31]:


data4=data.fillna(method='bfill')
data4


# In[ ]:




