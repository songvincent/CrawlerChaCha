#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[3]:


def S_search(pat,text,flag):
    '''
    re.search()的进化版
    '''
    res = ""
    if flag == None:
        con = re.search(pat,text)
    else:
        con = re.search(pat,text,flag)

    if con == None:
        res = ""
    else:
        res = con.groups()[0]
    
    return res


# In[ ]:




