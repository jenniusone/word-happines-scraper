#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


sns.set_style('darkgrid')
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = (10, 7)
plt.rcParams['figure.facecolor'] = '#FFE5B4'


# In[5]:


data = pd.read_csv (r"C://Users//ASUS//Downloads//world happines//world-happiness-report-2021.csv")


# In[6]:


data.head()


# In[7]:


data_columns = ['Country name', 'Regional indicator', 'Logged GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']


# In[8]:


data = data[data_columns].copy()


# In[9]:


happy_df = data.rename({'Country name' : 'country_name', 'Regional indicator' : 'regional_indicator', 'Logged GDP per capita' : 'logged_GDP_per_capita', 'Social support' : 'social_support', 'Healthy life expectancy' : 'healthy_life_expectancy', 'Freedom to make life choices' : 'freedom_to_make_life_choices', 'Generosity' :'generosity', 'Perceptions of corruption' : 'perceptions_of_corruption'}, axis=1)


# In[10]:


happy_df.head()


# In[11]:


happy_df.isnull().sum()


# In[12]:


# plot b/w social support and GDP 

plt.rcParams["figure.figsize"] = (15,7)
plt.title("Plot between Social Support and GDP ")
sns.scatterplot(x = happy_df.social_support, y = happy_df.logged_GDP_per_capita, hue = happy_df.regional_indicator,s = 200);
plt.legend(loc = 'upper left', fontsize = '10')
plt.xlabel ("social support")
plt.ylabel ("GDP per capita")


# In[17]:


gdp_region = happy_df.groupby('regional_indicator')['logged_GDP_per_capita'].sum()
gdp_region


# In[18]:


gdp_region.plot.pie(autopct = '%1.1f%%')
plt.title("GDP by region")
plt.ylabel ("")


# In[19]:


# total country

total_country = happy_df.groupby("regional_indicator")[["country_name"]].count()
print(total_country)


# In[20]:


# corruption in region 
corruption = happy_df.groupby('regional_indicator')[['perceptions_of_corruption']].mean()
corruption


# In[21]:


plt.rcParams['figure.figsize']=(12,8)
plt.title('perception of Corruption in various Regions')
plt.xlabel('region', fontsize = 15)
plt.ylabel('Corruption Index', fontsize = 15)
plt.xticks(rotation = 30, ha= 'right')
plt.bar(corruption.index, corruption.perceptions_of_corruption)


# In[22]:


top_10 = happy_df.head(10)
bottom_10 = happy_df.tail(10)


# In[23]:


fig, axes= plt.subplots(1,2, figsize= (16, 6))
plt.tight_layout(pad= 2)
xlabels= top_10.country_name
axes[0].set_title('top 10 happiest countries life expentancy')
axes[0].set_xticklabels(xlabels, rotation=45, ha='right')
sns.barplot(x=top_10.country_name, y= top_10.healthy_life_expectancy, ax= axes[0])
axes[0].set_xlabel('country_name')
axes[0].set_ylabel('Life Expectancy')

xlabels= bottom_10.country_name
axes[1].set_title('bottom 10 least happy countries life expentancy')
axes[1].set_xticklabels(xlabels, rotation=45, ha='right')
sns.barplot(x=bottom_10.country_name, y= bottom_10.healthy_life_expectancy, ax= axes[1])
axes[1].set_xlabel('country_name')
axes[1].set_ylabel('Life Expectancy')


# In[25]:


plt.rcParams['figure.figsize']=(12,8)
sns.scatterplot(x = happy_df.freedom_to_make_life_choices, y = happy_df.social_support, hue = happy_df.regional_indicator, s = 200)
plt.legend(loc= 'upper left', fontsize = '12')
plt.xlabel('freedom to make life choices')
plt.ylabel('sosial support')


# In[30]:


country = happy_df.sort_values(by='perceptions_of_corruption').head(10)
plt.rcParams['figure.figsize'] =(12,6)
plt.title('countries with most perceptions of corruption')
plt.xlabel('country', fontsize = 13)
plt.ylabel('corruption Index', fontsize = 13)
plt.xticks(rotation= 30, ha = 'right')
plt.bar(country.country_name, country.perceptions_of_corruption)

