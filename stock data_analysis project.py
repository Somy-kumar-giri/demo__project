#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd 
ds =pd.read_csv("C:/Users/drash/Downloads/stocks.csv")


# In[10]:


ds.head


# In[11]:


ds.tail


# In[12]:


ds.columns


# In[13]:


ds.info


# In[14]:


ds.nunique()


# In[15]:


ds.describe()


# In[16]:


ds.count()


# In[17]:


ds.shape


# In[18]:


ds.isnull()


# In[19]:


ds.dropna()


# In[20]:


import matplotlib.pyplot as plt
plt.plot(ds['Date'], ds['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Close Price Over Time')
plt.xticks(rotation=45)
plt.show()


# In[22]:


import matplotlib.pyplot as plt
plt.plot(ds['Date'], ds['Volume'])
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Volume Over Time')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




