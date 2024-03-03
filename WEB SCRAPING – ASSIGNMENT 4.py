#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# ## 1. Scrape the details of most viewed videos on YouTube from Wikipedia. Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details: 
# 
# A) Rank
# B) Name
# C) Artist
# D) Upload date
# E) Views

# In[71]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException


# In[72]:


driver= webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')
time.sleep(2)


# In[73]:


view =[]
rank =[]
name = []
artist=[]
upload_date= []


# In[74]:


try:
    v_name = driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody[1]/tr/td[1]')
    for i in v_name:
        name.append(i.text)
except NoSuchElementException:
    name.append('-')


# In[75]:


len(name)


# In[76]:


print(name)


# In[77]:


try:
    v_artist= driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody[1]/tr/td[2]')
    for i in v_artist:
        artist.append(i.text)
except NoSuchElementException:
    artist.append('-')


# In[78]:


len(artist)


# In[79]:


print(artist)


# In[80]:


try:
    v_view= driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody[1]/tr/td[3]')
    for i in v_view:
        view.append(i.text)
except NoSuchElementException:
    view.append('-')


# In[81]:


len(view)


# In[82]:


print(view)


# In[83]:


try:
    v_date= driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody[1]/tr/td[4]')
    for i in v_date:
        upload_date.append(i.text)
except NoSuchElementException:
    upload_date.append('-')


# In[84]:


len(upload_date)


# In[85]:


print(upload_date)


# In[86]:


try:
    v_rank= driver.find_elements(By.XPATH,'//table[@class="sortable wikitable sticky-header static-row-numbers sort-under col3center col4right jquery-tablesorter"]/tbody[1]/tr/td[0]')
    for i in v_rank:
        rank.append(i.text)
except NoSuchElementException:
    rank.append('-')


# In[87]:


len(rank)


# In[88]:


print(rank)


# In[89]:


Most_view= pd.DataFrame({'video_Name':name, 'Artist':artist,'Number_of_view_In_Billions':view,'Date_uploaded':upload_date})
Most_view


# ## Scrape the details team India’s international fixtures from bcci.tv.
# 
# Url = https://www.bcci.tv/.
# You need to find following details:
# A) Series
# B) Place
# C) Date
# D) Time
# Note: - From bcci.tv home page you have reach to the international fixture page through code.

# In[6]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[7]:


driver =webdriver.Chrome()
driver.get('https://www.bcci.tv/')

time.sleep(1)


# In[8]:


fixture_button = driver.find_element(By.XPATH,'//div[@class="tab-content bg-white w-100"]/div[2]/ul/div[1]/a[2]')
fixture_button.click()
time.sleep(1)


# In[9]:


series=[]
place=[]
date=[]
time=[]


# In[10]:


series_name = driver.find_elements(By.XPATH,'//h5[@class="match-tournament-name ng-binding"]')
for i in series_name:
    series.append(i.text)


# In[11]:


len(series)


# In[12]:


print(series)


# In[13]:


series_place = driver.find_elements(By.XPATH,'//div[@class="match-place ng-scope"]')
for i in series_place:
    place.append(i.text)


# In[14]:


len(place)


# In[15]:


print(place)


# In[16]:


dates = driver.find_elements(By.XPATH,'//div[@class="match-dates ng-binding"]')
for i in dates:
    date.append(i.text)


# In[17]:


len(date)


# In[18]:


print(date)


# In[19]:


s_time = driver.find_elements(By.XPATH,'//div[@class="match-time no-margin ng-binding"]')
for i in s_time:
    time.append(i.text)


# In[20]:


len(time)


# In[21]:


print(time)


# In[22]:


team_India_fixture = pd.DataFrame({'Series_Name':series,'Place':place, 'Date':date,'Time':time})
team_India_fixture


# In[ ]:





# # Scrape the details of State-wise GDP of India from statisticstime.com.
# Url = http://statisticstimes.com/
# You have to find following details: 
# A) Rank
# B) State
# C) GSDP(18-19)- at current prices
# D) GSDP(19-20)- at current prices
# E) Share(18-19)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code.

# In[55]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[56]:


driver = webdriver.Chrome()
driver.get('http://statisticstimes.com/')
driver.maximize_window()
time.sleep(2)


# In[57]:


home_button = driver.find_element(By.XPATH,'//div[@class="dropdown"][2]')
home_button.click()
button_click = driver.find_element(By.XPATH,'//div[@class="dropdown"][2]/div/a[3]')
button_click.click()


# In[64]:


gdp_of_state= driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
gdp_of_state.click()


# In[65]:


rank=[]
state =[]
gsdp_21_22 =[]
gsdp_22_23 =[]
share_21_22 =[]
gdp_in_billion =[]


# In[66]:


try:
    s_rank = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[1]')
    for i in s_rank:
        rank.append(i.text)
except NoSuchElementException:
    rank.append('-')


# In[67]:


print(rank)


# In[68]:


try:
    s_name = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[2]')
    for i in s_name:
        state.append(i.text)
except NoSuchElementException:
    state.append('-')


# In[69]:


print(state)


# In[70]:


try:
    gsdp_21 = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[4]')
    for i in gsdp_21:
        gsdp_21_22.append(i.text)
except NoSuchElementException:
    gsdp_21_22.append('-')


# In[71]:


print(gsdp_21_22)


# In[72]:


try:
    gsdp_22 = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[3]')
    for i in gsdp_22:
        gsdp_22_23.append(i.text)
except NoSuchElementException:
    gsdp_22_23.append('-')


# In[73]:


print(gsdp_22_23)


# In[74]:


try:
    share= driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[5]')
    for i in share:
        share_21_22.append(i.text)
except NoSuchElementException:
    share_21_22.append('-')


# In[75]:


print(share_21_22)


# In[76]:


try:
    s_gdp = driver.find_elements(By.XPATH,'//table[@id="table_id"]/tbody/tr/td[6]')
    for i in s_gdp:
        gdp_in_billion.append(i.text)
except NoSuchElementException:
    gdp_in_billion.append('-')


# In[77]:


print(gdp_in_billion)


# In[78]:


state_gdp= pd.DataFrame({'Rank':rank,'State':state,'GSDP_in_21_22':gsdp_21_22, 'GSDP_in_22_23':gsdp_22_23,'State_Share':share_21_22,'GDP_$Billion':gdp_in_billion})
state_gdp


# In[ ]:





# # Scrape the details of trending repositories on Github.com.
# 
# Url = https://github.com/
# 
# You have to find the following details:
# 
# A) Repository title
# 
# B) Repository description
# 
# C) Contributors count
# 
# D) Language used
# 
# Note: - From the home page you have to click on the trending option from Explore menu through code.

# In[123]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[124]:


driver= webdriver.Chrome()
driver.get('https://github.com/')
time.sleep(1)


# In[125]:


os_button= driver.find_element(By.XPATH,'//li[@class="HeaderMenu-item position-relative flex-wrap flex-justify-between flex-items-center d-block d-lg-flex flex-lg-nowrap flex-lg-items-center js-details-container js-header-menu-item"][3]')
os_button.click()
tranding_button= driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
tranding_button.click()


# In[126]:


title=[]
discription=[]
c_count=[]
language=[]


# In[127]:


try:
    r_title = driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]/a')
    for i in r_title:
        title.append(i.text)
except NoSuchElementException:
    title.append('------')


# In[128]:


print(title)


# In[129]:


len(title)


# In[130]:


try:
    discr = driver.find_elements(By.XPATH,'//article[@class="Box-row"]/p')
    for i in discr:
        discription.append(i.text)
except NoSuchElementException:
    discription.append('------')


# In[131]:


print(discription)


# In[132]:


len(discription)


# In[133]:


try:
    conti = driver.find_elements(By.XPATH,'//span[@class="d-inline-block mr-3"]')
    for i in conti:
        c_count.append(i.text)
except NoSuchElementException:
    c_count('------')


# In[134]:


print(c_count)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Scrape the details of top 100 songs on billiboard.com. 
# Url = https:/www.billboard.com/ You have to find the following details:
# 
# A) Song name
# B) Artist name
# C) Last week rank
# D) Peak rank
# E) Weeks on board
# Note: - From the home page you have to click on the charts option then hot 100-page link through code.

# In[135]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[138]:


driver = webdriver.Chrome()
driver.get('https:/www.billboard.com/')
time.sleep(1)


# In[140]:


Y_E_C_button = driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[2]/div/div/div[2]/div[2]/div/div/nav/ul/li[1]')
Y_E_C_button.click()
time.sleep(1)


# In[141]:


fchart_button = driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[3]')
fchart_button.click()
time.sleep(1)


# In[142]:


s_name=[]
artist =[]
last_w_rank =[]
p_rank=[]
weeks_on_board=[]


# In[143]:


try:
    sname = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li/h3')
    for i in sname:
        s_name.append(i.text)
except NoSuchElementException:
    s_name.append('-')
    
try:
    aname = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[1]/span')
    for i in aname:
        artist.append(i.text)
except NoSuchElementException:
    artist.append('-')

try:
    l_w_r = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[4]/span')
    for i in l_w_r:
        last_w_rank.append(i.text)
except NoSuchElementException:
    last_w_rank.append('-')

try:
    peak= driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[5]/span')
    for i in peak:
        p_rank.append(i.text)
except NoSuchElementException:
    p_rank.append('-')

try:
    on_board = driver.find_elements(By.XPATH,'//li[@class="lrv-u-width-100p"]/ul/li[6]/span')
    for i in on_board:
        weeks_on_board.append(i.text)
except NoSuchElementException:
    weeks_on_board.append('-')


# In[144]:


Billboard_Hot_100 = pd.DataFrame({'Song_Name':s_name,'Artist':artist,'Last_week_rank':last_w_rank,'Peak_rank':p_rank,'Weeks_on_board':weeks_on_board})
Billboard_Hot_100


# In[ ]:





# # Scrape the details of Highest selling novels.
# 
# A) Book name
# B) Author name
# C) Volumes sold
# D) Publisher
# E) Genre
# 
# Url - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare

# In[145]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[146]:


driver = webdriver.Chrome()
driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')
time.sleep(1)


# In[147]:


book_name=[]
author =[]
volumes=[]
publisher=[]
genre=[]


# In[148]:


try:
    bname= driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[2]')
    for i in bname:
        book_name.append(i.text)
except NoSuchElementException:
    book_name.append('-')
try:
    bauthor=driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[3]')
    for i in bauthor:
        author.append(i.text)
except NoSuchElementException:
    author.append('-')
try:
    vols = driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[4]')
    for i in vols:
        volumes.append(i.text)
except NoSuchElementException:
    volumes.append('-')
try:
    publis = driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[5]')
    for i in publis:
        publisher.append(i.text)
except NoSuchElementException:
    publisher.append('-')
try:
    gen = driver.find_elements(By.XPATH,'//div[@class="embed block"]/table/tbody/tr/td[6]')
    for i in gen:
        genre.append(i.text)
except NoSuchElementException:
    genre.append('-')


# In[149]:


Top_Books= pd.DataFrame({'Book_Title':book_name,'Author':author,'Volumes_sold':volumes,'Publisher':publisher,'Genre':genre})
Top_Books


# In[ ]:




