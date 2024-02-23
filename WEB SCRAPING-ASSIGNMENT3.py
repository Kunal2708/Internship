#!/usr/bin/env python
# coding: utf-8

# In[66]:


get_ipython().system('pip install selenium')


# ## 1. Write a python program which searches all the product under a particular product from www.amazon.in. The product to be searched will be taken as input from user. 
# 
# For e.g. If user input is ‘guitar’. Then search for guitars.
# 
# ## 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. 
# 
# In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: 
# 
# "Brand Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.

# In[43]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[44]:


driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
time.sleep(5)


# In[45]:


# User Input prompt
user_input = input('Search in world of Amazon :')


# In[46]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys(user_input)


# In[ ]:





# In[47]:


search_button = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_button.click()


# In[48]:


Brand_Name =[] 
Name_of_the_Product =[] 
Price =[] 
Return_Exchange =[] 
Expected_Delivery =[] 
Availability =[]  
Product_URL = []


# In[49]:


start = 0
end = 3


# In[50]:


for page in range(start,end):
    url = driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        Product_URL.append(i.get_attribute("href"))
    next_button = driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    next_button.click()
    time.sleep(3)


# In[ ]:





# In[52]:


for url in Product_URL:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand= driver.find_element(By.XPATH,'//div[@class="a-section a-spacing-small a-spacing-top-small"]/table/tbody/tr[1]/td[2]/span')
        Brand_Name.append(brand.text)
    except NoSuchElementException:
        Brand_Name.append('-')
    try:
        price = driver.find_element(By.XPATH,'//div[@class="a-section"]/span/span/span[2]')
        Price.append(price.text)
    except NoSuchElementException:
        Price.append('-')
    try:
        exchange = driver.find_element(By.XPATH,'//ol[@class="a-carousel"]/li[3]/div/span/div[2]/span')
        Return_Exchange.append(exchange.text)
    except NoSuchElementException:
        Return_Exchange.append('-')
    try:
        name = driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        Name_of_the_Product.append(name.text)
    except NoSuchElementException:
        Name_of_the_Product.append('-')
    try:
        delivery = driver.find_element(By.XPATH,'//div[@class="a-spacing-base"][2]/span/span')
        Expected_Delivery.append(delivery.text)
    except NoSuchElementException:
        Expected_Delivery.append('-')
    try:
        availability =driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-success"]')
        Availability.append(availability.text)
    except NoSuchElementException:
        Availability.append('-')


# In[54]:


len(Product_URL), len(Brand_Name), len(Price),len(Return_Exchange),len(Name_of_the_Product),len(Expected_Delivery),len(Availability)


# In[60]:


import pandas as pd
df =pd.DataFrame({'Product_Name': Name_of_the_Product, 'Brand': Brand_Name, 'Price': Price,  'Expected_Delivery':Expected_Delivery,'Return/Exchange': Return_Exchange})
df


# In[ ]:





# In[62]:


df.to_csv('assignment3_Q2.csv', index=True)


# In[63]:


time.sleep(2)
driver.close()


# In[ ]:





# ## Q3 Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.

# In[82]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[83]:


driver =webdriver.Chrome()
driver.get('https://images.google.com/')
time.sleep(2)


# In[84]:


u_input = input('Enter Name to search : ')


# In[85]:


search = driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]')
search.clear()
search.send_keys(u_input)
search_button = driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search_button.click()


# In[91]:


for _ in range(10):
    driver.execute_script('window.scrollBy(0,100)')
img_urls =[]
images = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for image in images:
    source = image.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)

import requests
for i in range(len(img_urls)):
    if i>10:
        break
    print('Downloading {0} of {1} impages'.format(i+1,10))
    response = requests.get(img_urls[i])
    file = open(r"C:\Users\kdmod\OneDrive\kunal\DS"+str(i)+".jpg","wb")
    file.write(response.content)
                                


# In[92]:


time.sleep(2)
driver.close()


# In[ ]:





# # Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: 
# 
# “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[171]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[172]:


driver = webdriver.Chrome()
driver.get('https://www.flipkart.com/')
time.sleep(2)


# In[173]:


smart_ph_name = input('Enter Smart Phone Brand :')


# In[174]:


search = driver.find_element(By.XPATH,'//input[@class="Pke_EE"]')
search.send_keys(smart_ph_name)
search_button = driver.find_element(By.XPATH,'//button[@class="_2iLD__"]')
search_button.click()


# In[175]:


brand_name =[]
phone_colour =[]
phone_ram=[]
phone_storage=[]
primary_camera=[]
secondary_camera=[]
display_size=[]
battery =[]
price=[]


# In[176]:


phone_url =[]
url = driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    phone_url.append(i.get_attribute("href"))


# In[177]:


len(phone_url)


# In[178]:


for url in phone_url:
    driver.get(url)
    time.sleep(2)
    
    read_more = driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    read_more.click()
    try:
        brand= driver.find_element(By.XPATH,'//span[@class="B_NuCI"]')
        brand_name.append(brand.text)
    except NoSuchElementException:
        brand_name.append('-')
    try:
        mrp = driver.find_element(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')
        price.append(mrp.text)
    except NoSuchElementException:
        price.append('-')
    try:
        colour = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][1]/table/tbody/tr[4]/td[2]/ul/li')
        phone_colour.append(colour.text)
    except NoSuchElementException:
        phone_colour.append('-')
    try:
        ram= driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table/tbody/tr[2]/td[2]')
        phone_ram.append(ram.text)
    except NoSuchElementException:
        phone_ram.append('-')
    try:
        storage = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][4]/table/tbody/tr[1]/td[2]')
        phone_storage.append(storage.text)
    except NoSuchElementException:
        phone_storage.append('-')
    try:
        main_camera = driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table/tbody/tr[2]/td[2]')
        primary_camera.append(main_camera.text)
    except NoSuchElementException:
        primary_camera.append('-')
    try:
        second_camera= driver.find_element(By.XPATH,'//div[@class="_3k-BhJ"][5]/table/tbody/tr[4]/td[2]')
        secondary_camera.append(second_camera.text)
    except NoSuchElementException:
        secondary_camera.append('-')
    try:
        display = driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li[2]')
        display_size.append(display.text)
    except NoSuchElementException:
        display_size.append('-')
    try:
        batry = driver.find_element(By.XPATH,'//div[@class="_2418kt"]/ul/li[4]')
        battery.append(batry.text)
    except NoSuchElementException:
        battery.append('-')


# In[179]:


len(brand_name),len(price), len(phone_colour), len(phone_ram),len(phone_storage), len(primary_camera), len(secondary_camera), len(display_size), len(battery)


# In[180]:


phone_df= pd.DataFrame({'Phone_Name':brand_name, 'Price': price, 'Colour':phone_colour, 'RAM':phone_ram, 'Storage':phone_storage, 'Primary_Camera': primary_camera, 'Secondary_Camera':secondary_camera, 'Display_Size':display_size, 'Battery': battery, 'URL':phone_url})
phone_df
                      


# In[181]:


phone_df.to_csv('assignment3_Q4.csv', index=True)


# In[182]:


time.sleep(2)
driver.close()


# In[ ]:





# In[ ]:





# # Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[196]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[197]:


driver= webdriver.Chrome()
driver.get('https://maps.google.com/')
time.sleep(2)

city_input= input('Enter Name of City -')


# In[198]:


search =driver.find_element(By.XPATH,'//input[@class="searchboxinput xiQnY"]')
search.send_keys(city_input)
search_button1 = driver.find_element(By.XPATH,'//span[@class="google-symbols"]')
search_button1.click()


# In[199]:


Current_URL=driver.current_url
print('URL of current search :',Current_URL)

try:
    if "@" in Current_URL:
        location=current_url.split('@')[1].split(',*/data')[0].split(',')
        location
        print('Latitude of given Location:',location[0])
        print('Longitude of given Location:',location[1])
except:
    print('Location detail not found in URL')


# In[ ]:





# In[ ]:





# ## Write a program to scrap all the available details of best gaming laptops from digit.in.

# In[205]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[206]:


driver= webdriver.Chrome()
driver.get('https://www.digit.in/top-products/best-gaming-laptops-40.html')
time.sleep(2)


# In[207]:


Laptop_name = []
Price =[]
Retailer =[]
URL =[]


# In[222]:


name = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/article/div[5]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/h3')
Laptop_name.append(name.text)

price= driver.find_element(By.XPATH,'//div[@class="cegg-price-row"]')
Price.append(price.text)

retailer = driver.find_element(By.XPATH,'//small[@class="text-muted title-case"]')
Retailer.append(retailer.text)


# In[223]:


len(Laptop_name), len(Price), len(Retailer)


# In[ ]:





# In[ ]:





# # Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.

# In[255]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[256]:


driver = webdriver.Chrome()
driver.get('https://www.forbes.com/')
time.sleep(2)


# In[263]:


menu = driver.find_element(By.XPATH,'//div[@class="_69hVhdY4"]')
menu.click()
submenu = driver.find_element(By.XPATH,'//div[@class="mpBfVZz3"]')
submenu.click()
innermenu = driver.find_element(By.XPATH,'//li[@class="TjJgrPSg _2bNo56RE secondary"]')
innermenu.click()


# In[251]:





# # Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted from any YouTube Video.

# In[265]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# In[290]:


driver = webdriver.Chrome()
driver.get('https://www.youtube.com/?gl=GB&hl=en-GB')
time.sleep(5)


# In[291]:


tag_line = ('Nature Sounds - Birds Singing Without Music, 24 Hour Bird Sounds Relaxation, Soothing Nature Sounds')


# In[292]:


ytsearch = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
ytsearch.send_keys(tag_line)
time.sleep(2)
ytsearch_button = driver.find_element(By.XPATH,'//button[@class="style-scope ytd-searchbox"]/yt-icon/yt-icon-shape')
ytsearch_button.click()


# In[293]:


video = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
video.click()                           


# In[295]:


user_comment =[]
comment = driver.find_element(By.XPATH,'//yt-formatted-string[@class ="style-scope ytd-video-renderer"]')



# In[296]:


for _ in range(20):
    driver.execute_script('window.scrollBy(0,1000)')


# In[ ]:





# In[ ]:




