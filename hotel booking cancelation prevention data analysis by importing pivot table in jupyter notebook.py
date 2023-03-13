#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import os


# In[2]:


df=pd.read_csv("hotel_booking.csv")


# In[3]:


df.head()


# In[4]:


get_ipython().system('pip install pivot_table')


# In[5]:


pip install pivottablejs


# In[7]:


from pivottablejs import pivot_ui


# In[8]:


pivot_ui(df)

