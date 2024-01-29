#!/usr/bin/env python
# coding: utf-8

# # 1) Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[1]:


get_ipython().system('pip  install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[3]:


soup = BeautifulSoup(page.content)
soup


# In[8]:


headers = soup.find_all('span', class_ ='mw-headline')
headers


# In[ ]:





# In[10]:


headers =[]
for i in soup.find_all('span', class_= 'mw-headline'):
    headers.append(i.text)
    
headers
    


# In[12]:


import pandas as pd
df = pd.DataFrame({'Header' : headers})
df


# In[ ]:





# # Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[69]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://presidentofindia.nic.in/former-presidents')
page


# In[70]:


soup = BeautifulSoup(page.content)
soup


# In[38]:


president = soup.find_all('div', class_ ='desc-sec')
president


# In[87]:


president=[]
for i in soup.find_all('div', class_= 'desc-sec'):
        president.append(i.text.replace('\n',' | '))
    
president
    


# In[88]:


import pandas as pd
df = pd.DataFrame({'Former President and Their term' : president})
df


# In[ ]:





# In[ ]:





# # Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# 
# c) Top 10 ODI bowlers along with the records of their team andrating.

# In[97]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.icc-cricket.com/rankings/team-rankings/mens/odi')
page


# In[98]:


soup = BeautifulSoup(page.content)
soup


# In[179]:


team=[]
for i in soup.find_all('div', class_='si-text'):
    team.append(i.text)
team


# In[ ]:





# In[181]:


matches = []
for i in soup.find_all('div', class_="si-text"):
    matches.append(i.text)
matches


# In[102]:


#raised ticket for this one as can not find where I am doing mistake


# In[ ]:





# In[ ]:





# # 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# 
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[ ]:





# In[ ]:





# # 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
# i) Headline
# 
# ii) Time
# 
# iii) News Link

# In[107]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.cnbc.com/world/?region=world')
page


# In[129]:


soup = BeautifulSoup(page.content)
soup


# In[139]:


time =[]
for i in soup.find_all('time', class_='LatestNews-timestamp'):
    time.append(i.text)
    
time
#headline = soup.find_all('div',class_='LatestNews-container')
#headline


# In[136]:


headline =[]
for i in soup.find_all('a', class_="LatestNews-headline"):
    headline.append(i.text)
    
headline


# In[144]:


link =[]
for i in soup.find_all('a', class_='LatestNews-headline'):
    link.append(i.text)
    
link


# In[147]:


import pandas as pd
df = pd.DataFrame({'Time' : time,'Headline' : headline, 'Link' :link})
df


# In[ ]:





# # 6) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
# i) Paper Title
# 
# ii) Authors
# 
# iii) Published Date
# 
# iv) Paper URL

# In[149]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[150]:


soup = BeautifulSoup(page.content)
soup


# In[151]:


title =[]
for i in soup.find_all('h2', class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg'):
    title.append(i.text)
title


# In[152]:


author = []
for i in soup.find_all('span', class_='sc-1w3fpd7-0 dnCnAO'):
    author.append(i.text)
author


# In[153]:


date =[]
for i in soup.find_all('span', class_='sc-1thf9ly-2 dvggWt'):
    date.append(i.text)
date


# In[156]:


link = []
for i in soup.find_all('a', class_='sc-5smygv-0 fIXTHm'):
    link.append(i.text)
link


# In[157]:


import pandas as pd
df = pd.DataFrame({'Paper Title' : title,'Author' : author, 'Published Date': date, 'Link' :link})
df


# In[ ]:





# In[ ]:





# In[ ]:





# # 7) Write a python program to scrape mentioned details from dineout.co.in and make data frame-
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[158]:


# Can not open pade in uk. 
# I have tried to look for similar sites in UK but all of them have respose rate above 400 but found one which I have tried to do it.


# # ![Screenshot%202024-01-27%20121536.png](attachment:Screenshot%202024-01-27%20121536.png)

# In[3]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.timeout.com/london/food-and-drink/londons-best-sunday-lunches')
page


# In[9]:


soup = BeautifulSoup(page.content)
soup


# In[24]:


name =[]
for i in soup.find_all('div',class_="_title_kc5qn_9"):
    name.append(i.text.replace('\xa0',' - '))

name [0:15]


# In[23]:


info =[]
for i in soup.find_all('div',class_="_tileTags_kc5qn_44"):
    info.append(i.text)
info [0:15]


# In[22]:


import pandas as pd
df = pd.DataFrame({'Ranking and Name': name, 'Location and type':info  })
df


# In[ ]:





# In[ ]:




