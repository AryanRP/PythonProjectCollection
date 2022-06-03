#!/usr/bin/env python
# coding: utf-8

# In[2]:


# strip the input string, if there is no space then remove the input string from the string


# In[3]:


import re


# In[20]:


def stripp(input1,removal):
#check if the string needs stripping
    if input1 != input1.strip():
        out=input1.strip()
        return out
#identify if the string exists in the string
    find=re.compile(removal)
    if find.search(input1)== None:
        print("There is nothing to remove!")
    else:
#remove the string
        out=input1.replace(removal,"")
        return out


# In[21]:


stripp("Aryan is hungry","hungry")


# In[ ]:




