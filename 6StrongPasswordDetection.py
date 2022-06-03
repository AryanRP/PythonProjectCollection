#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a strong password has at least eight characters
# both lower and upper case and at least one number


# In[2]:


import re


# In[18]:


password=input("Please type in your password! ")
# does the password include eight characters?
PassSearch1=re.compile(r'\w{8,}')
# does the password include at least one number?
PassSearch2=re.compile(r'\d{1,}')
# does the password has a lowercase?
PassSearch3=re.compile(r'[a-z]')
# does the password has a uppercase?
PassSearch4=re.compile(r'[A-Z]')


if PassSearch1.search(password)== None:
    print("Not Enough Characters!")
elif PassSearch2.search(password)== None:
    print("No numbers were included!")
elif PassSearch3.search(password)== None:
    print("No lowercase found !")
elif PassSearch4.search(password)== None:
    print("No uppercase found!")
else:
    print("Exellent password !")

