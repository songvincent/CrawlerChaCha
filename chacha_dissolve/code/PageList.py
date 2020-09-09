#!/usr/bin/env python
# coding: utf-8

# In[2]:


## 获得所有详情页的pagelist


# In[1]:


from selenium import webdriver
import time
import re
from util import *
import requests


# In[2]:


class PageList:
    
    def __init__(self,tpolicy):
        self.content = []
        
        self.title = ""
        self.url = ""
        self.area = ""
        self.valid_scope = ""  ##有效期间
        self.sup_ind = ""
        
        self.tpolicy = tpolicy
        
        self.index2pol = {}
        self.index2pol['6'] = 'regu_item'
        self.index2pol['5'] = 'sup_item'
#         self.index2pol['3'] = 'imple_regu'
        
    def get_data(self):
        ### 标题
        policy = self.tpolicy[2]
        title = S_search('<div class="policy-title">.*?<span.*?>(.*?)</span>.*?</div>',policy,re.S)
        self.title = title.replace('&nbsp;','')
        ### url
        url_id = self.tpolicy[0]
        data_type = self.tpolicy[1]
        self.url = 'https://www.chacha.top/{}?id='.format(self.index2pol[data_type])+url_id
        ### 数据类型
#         self.poltype = self.index2pol_en[data_type]
        ### 适用区域
        area = S_search('<span class="pull-left.*?">适用地区(.*?)</span>',policy,re.S)
        self.area = '适用地区'+area
        
        ### 有效期限
        valid_scope = S_search('<span class="pull-left.*?">有效期限(.*?)</span>',policy,re.S)
        valid_scope = re.sub('<.*?>','',valid_scope)
        self.valid_scope = '有效期限'+valid_scope
        
        ### 支持行业
        pat = r'<span class="pull-left m-r-md text-gray sup-ind">.*?<span>(.*?)</span></span></div>'
        sup_ind = S_search(pat,policy,re.S)
        self.sup_ind = "适用行业："+sup_ind
        
    def handle_content(self):
        self.get_data()
#         tb1 = ['标题','详情页','适用区域',','有效期限','适用行业']
        self.content =[self.title,self.url,self.area,self.valid_scope,self.sup_ind]


# In[21]:


if __name__ == '__main__':
#     url = 'https://www.chacha.top/origin?area=true'
    url = 'https://www.chacha.top/sup?area=true'
    path1 = '../sfdrive/geckodriver.exe'
    browser = webdriver.Firefox(executable_path = path1)
    browser.get(url)
    time.sleep(1)
    
    text = browser.page_source
    
    pat = r'<ul class="clearfix policy-data">(.*?)</ul>'
    con = re.search(pat,text,re.S)
    con = con.groups()[0]

    lipat = r'<li class="sup-list-item m-b-md".*?data-id="(.*?)" data-type="(.*?)">(.*?)</li>'
    policy_lst = re.findall(lipat,con,re.S)
    
    length = len(policy_lst)
    print(length)
    for i in range(length):
        plist = PageList(policy_lst[i])
        plist.handle_content()
        print(plist.content)


# In[ ]:




