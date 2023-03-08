#!/usr/bin/env python
# coding: utf-8

# # Data Analysis Project of hotel booking cancelations

# # steps to do the project:

# step 1:
#             Ask questions like what is the problem and what do you want to change and many more questions you should ask before further procedings.
#     
# step 2:
#     According to the qustions asked by the client then prepare some problem statements on our own.
# 
# step 3:
#     Then gather the data from client and identify the data you want to analyze.
# 
# step 4:
#     Do some exploratory data analysis and do some cleaning of the data.
# 
# step 5:
#     Then analyze the data to get some useful insights from it.
# 
# step 6:
#     Present the data in terms of reports or dashboards using visualizations tools to make easy understand.
# 

# # Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import os
import seaborn as sns
import sys


# # Loading the data set

# In[2]:


hotelData=pd.read_csv("hotel_booking.csv")


# # Exploratory Data Analysis and Data cleaning

# In[3]:


hotelData


# In[4]:


hotelData.info()


# In[5]:


hotelData.describe()


# In[6]:


hotelData.size


# In[7]:


hotelData.shape


# In[8]:


hotelData.head()


# In[9]:


hotelData.tail()


# In[10]:


hotelData.info()


# # removing the unwanted columns which will not effect in resultant of hotel booking

# In[11]:


hoteldata=hotelData.drop(['name','email','phone-number','credit_card'],axis=1)


# In[12]:


hoteldata.columns


# In[13]:


hoteldata.info()


# # converting date object into datetime

# In[14]:


hoteldata['reservation_status_date']=pd.to_datetime(hoteldata['reservation_status_date'])


# In[15]:


hoteldata.info()


# In[16]:


hoteldata.describe()


# # finding the statistics only for object columns

# In[17]:


hoteldata.describe(include='object')


# In[18]:


for i in hoteldata.describe(include='object').columns:
    print(i)
    print(hoteldata[i].unique())
    print('-'*20)


# In[19]:


hoteldata.isnull().sum()


# # removing outliers which we can't make use to get results and not easy to handle those outliers

# In[20]:


hoteldata.drop(['agent','company'],axis=1, inplace=True)


# In[21]:


hoteldata.info()


# # those we can remove of less missing values of respective rows we will do as below

# In[22]:


hoteldata.dropna(inplace=True)


# In[23]:


hoteldata.isnull().sum()


# In[24]:


hoteldata.describe()


# In[25]:


hoteldata['adr'].plot(kind='box')


# # removing the outlier in adr

# In[26]:


hoteldata=hoteldata[hoteldata['adr']<5000]


# In[27]:


hoteldata.describe()


# # Data analysis and visualization

# finding cancelled_percentage 

# In[28]:


canceled_percentage=hoteldata['is_canceled'].value_counts(normalize=True)


# In[29]:


canceled_percentage


# In[78]:


plt.figure(figsize=(5,3))
plt.title('Reservation status count')
plt.ylabel('numer of reservations')
plt.bar(['Not canceled','canceled'],hoteldata['is_canceled'].value_counts(),color='y',edgecolor='r',width=0.2)


# The above bargraphs shows the percentage of reservations that are canceled and those that are not.
# it is obvious that there are still a significant number of reservations that have not been canceld.
# there are still 37% of clients who canceled their reservations, which has a significant impact on the hotel's earnings.

# In[31]:


plt.figure(figsize=(8,4))
ax1=sns.countplot(x='hotel',hue='is_canceled',data=hoteldata,palette='deep')
legend_labels,_= ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels',size=20)
plt.xlabel('hotel')
plt.ylabel('numer of reservations')
plt.show()


# In comparision to resort hotels, city hotels have more bookings. It's possible that resort hotels are more expensive than those city hotels.

# In[32]:


resort_hotel = hoteldata[hoteldata['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[33]:


city_hotel = hoteldata[hoteldata['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# therefore we can observe that in resort hotel the cancelation percentage is lesser than that of city hotel let see what will be the reason behind of it.

# In[34]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[47]:


plt.figure(figsize=(25,10))
plt.title('Average Daily Rate in city and Resort Hotel',fontsize=25)
plt.plot(resort_hotel.index,resort_hotel['adr'],label='Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label='City Hotel')
plt.legend(fontsize=15)
plt.show()


# The line graph above shows that on certain days the average daily rate for a city hotel is less than that of a resort hotel, and on other days, it is even less. It goes without saying that weekends and holidays may see a rise in resort hotel rates.

# In[48]:


hoteldata['month']=hoteldata['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1=sns.countplot(x='month',hue='is_canceled',data=hoteldata)


# we have developed the grouped bar chart to analyze the months with the highest and lowest reservations levels according to the reservations status. As we can see both the number of confirmed reservations and the number of canceled reservations are largest in the months of august and september whereas in january the most canceled resrvations. 

# In[57]:


plt.figure(figsize = (14,8))
plt.title('adr per month',fontsize=25)
sns.barplot('month','adr',data=hoteldata[hoteldata['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# This bar graph shows that cancelations are most common when prices are greatest and are leasat common when they are lowest. Therefore, the cost of the accomodations is solely responsible for the cancelations.
# let's see which country has the higest reservations canceled. The top country is portugal with the higest number of cancelations.

# In[62]:


canceled_data = hoteldata[hoteldata['is_canceled']==1]
top_10_country = canceled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct = '%.3f', labels = top_10_country.index)
plt.show()


# In[63]:


hoteldata['market_segment'].value_counts()


# In[66]:


hoteldata['market_segment'].value_counts(normalize=True)


# In[68]:


canceled_data['market_segment'].value_counts(normalize=True)


# let's check the area from where guests are visiting the hotels and making reservations. is it coming from direct or groups, online or offline travel agencies? 
# around 47% of the clients, where as 27% come from groups. only 4% of clients book hotels directly by visiting then and making reservations.

# # review points and suggestions to the hotels

# cancelations rates rise as the price went up.
# in order to prevent cancelations of reservations, hotels could work on their pricing strategies and try to lower the rates for specific hotels based on locations. 
# also need to provide some discounts to the customers so that they wont canceled much reservations.

# As the ratio of the cancelations and not cancelation of the resort hotels is higher in the resort hotel than the city hotels.
# So the hotels should provide a resonable discount on the room prices on weekends or on holidays to avoid the cancelations.

# In the month of january, hotels can start campains or do some marketing with a resonable amount of increase their revenue as the cancelation is the highest in this month.

# They can also increase the quality of their hotels and their services mainly in portugal to reduce the cancelation rate.
