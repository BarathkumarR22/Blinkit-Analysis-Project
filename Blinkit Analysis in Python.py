#!/usr/bin/env python
# coding: utf-8

# ## **DATA ANALYSIS PYTHON PROJECT - BLINKIT ANALYSIS**

# ## Import Libraries

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# ## Import Raw Data 

# In[2]:


df= pd.read_csv("C:/Users/barat/Downloads/blinkit_data.csv")


# ## Size of Data

# In[3]:


print ("Size of Date:",df.shape)


# ## Field Info

# In[4]:


df.columns


# ## Data Types

# In[5]:


df.dtypes


# ## Data Cleaning

# In[6]:


print(df['Item Fat Content'].unique())


# In[7]:


df['Item Fat Content']= df['Item Fat Content'].replace({'LF':'Low Fat','low fat':'Low Fat','reg' :'Regular'})


# In[8]:


print(df['Item Fat Content'].unique())


# ## **Business Requirements**

# ## KPI Requirements

# In[9]:


# Total Sales 
total_sales= df['Sales'].sum()
# Average Sales
avg_sales= df['Sales'].mean()
# No of Item Sold 
no_of_items_sold = df['Sales'].count()
# Average_Ratings 
avg_ratings = df['Rating'].mean()
print(f"Total Sales: ${total_sales:,.1f}")
print(f"Average Sales: ${avg_sales:,.1f}")
print(f"No_of_Items_Sold: {no_of_items_sold:,.0f}")
print(f"Average Ratings: {avg_ratings:,.1f}")


# ## Chart Requirements

# ##### Total Sales by Fat Content

# In[10]:


sales_by_fat = df.groupby('Item Fat Content') ['Sales'].sum()
plt.pie(sales_by_fat,labels= sales_by_fat.index,
        autopct = '%.1f%%',
        startangle = 90)
plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()


# ### Total Sales By Type

# In[11]:


sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending = False)
plt.figure(figsize=(10,6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)

plt.xticks(rotation= -90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,bar.get_height(),
             f'{bar.get_height():,.0f}',ha='center',va='bottom',fontsize=8)
plt.tight_layout()
plt.show()


# #### Fat Content by Outlet for Total Sales 

# In[12]:


grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped= grouped[['Regular','Low Fat']]

ax= grouped.plot(kind='bar',figsize=(8,5),title='Outlet Tier by Item Fat Content')
plt.xlabel('Outlet Location tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()


# In[14]:


sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()
plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index,sales_by_year.values,marker='o',linestyle='-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x,y in zip(sales_by_year.index,sales_by_year.values):
    plt.text(x,y,f'{y:,.0f}',ha='center',va='bottom',fontsize=8)
plt.tight_layout()
plt.show()


# ### Sales by Outlet Size

# In[16]:


sales_by_size = df.groupby('Outlet Size')['Sales'].sum()
plt.figure(figsize=(4,4))
plt.pie(sales_by_size, labels=sales_by_size.index,autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()


# ### Sales by Outlet Location

# In[17]:


sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales',ascending=False)
plt.figure(figsize=(8,3))
ax=sns.barplot(x='Sales',y='Outlet Location Type',data=sales_by_location)
plt.title('Total Sales by Outlet Locaton Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')
plt.tight_layout()
plt.show()


# In[ ]:




