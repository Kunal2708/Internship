#!/usr/bin/env python
# coding: utf-8

# # 1.  Which of the following operators is used to calculate remainder in a division? 
# Ans - C) %  
# 

# # 2. In python 2//3 is equal to? 
# 
# Ans  B) 0 

# # 3. In python, 6<<2 is equal to? 
# 
# Ans - C) 24

# # 4. In python, 6&2 will give which of the following as output? 
# Ans A) 2 

# # 5. In python, 6|2 will give which of the following as output? 
# 
# Ans - D) 6 

# # 6. What does the finally keyword denotes in python? 
# Ans - C) the finally block will be executed no matter if the try block raises an error or not. 
# 

# # 7. What does raise keyword is used for in python? 
# Ans - A) It is used to raise an exception. 

# # 8. Which of the following is a common use case of yield keyword in python? 
# Ans -A) in defining an iterator 

# # 9. Which of the following are the valid variable names? 
# Ans  - A) _abc &  C) abc2 

# # 10. Which of the following are the keywords in python? 
# Ans - A) yield B) raise 

# In[15]:


import keyword
print(keyword.kwlist)


# # 11 Write a python program to find the factorial of a number

# In[17]:


num = int(input('Enter any digit -  '))
if num <1:
    print ('enter only positive number')
factorial = 1
if num >=1:
    for F in range (1,num+1):
        factorial = factorial*F
    print ('factorial of Number', num,'is', factorial)


# # 12. Write a python program to find whether a number is prime or composite.

# In[19]:


Num = int(input('Enter any positive number - '))
if Num >1:
    for i in range (2, Num):
        if (Num%i) ==0:
            print('Your input number',Num, 'is Composite')
            break
        else: 
            print('Your input number',Num, 'is Prime')
            break
elif Num ==0 or Num ==1:
    print('* * *Your input number',Num, 'is not Prime or Composite')


# In[ ]:





# # 13. Write a python program to check whether a given string is palindrome or not.

# In[ ]:


# Sorry can not solve it


# In[ ]:





# # 14. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[20]:


import pandas as pd
from math import sqrt
Side1 = float(input('Enter Side 1- '))
Side2 = float(input('Enter Side 2- '))
Side3 = sqrt((Side1*Side1)+(Side2*Side2))
print('Value of Side 3 is', Side3)


# # 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[18]:


#sorry


# In[ ]:




