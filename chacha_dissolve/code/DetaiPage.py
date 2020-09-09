#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import re
from util import *
import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


import pyhanlp
from pyhanlp import *


# In[4]:


class DetailPage:
    
    def __init__(self,url):
        
        self.source = ""
        self.money = ""
        self.next_url = ""
        self.nxtitle = ""
        self.sup_ind = ""
        self.mbody = ""
        
        self.url = url
        self.s = ""
        
#         self.material = None
    
    def handle_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        r = requests.get(self.url,headers=headers, timeout=6)
        s = r.content.decode('utf-8')  ## decode
        self.s = s
    
    def handle_source(self):   ###（数据来源）
        pat = '<div class="policy-source-con"><.*?>数据来源：(.*?)</div>'
        self.source = S_search(pat,self.s,re.S)
#         print(self.source)
        
    def handle_money(self):  ### 扶持金额（力度）
        
        pat = '<span class="sup-money m-r-md">扶持金额：<span>(.*?)</span></span>'
        money = S_search(pat,self.s,re.S)
        self.money = money.replace('&nbsp;','')
#         print(self.money)

    def handle_nexturl(self):
        
        pat = r'"sup_policy":\[\{"policy_id":"(.*?)"'
        url_id = S_search(pat,self.s,re.S)
        self.next_url = 'https://www.chacha.top/sup_policy?id='+ url_id
        
    def handle_next_title(self):  ## 处理项目来源
        
        pat = r'<a.*?class="file-download".*?>(.*?)</a>'
        nt = S_search(pat,self.s,re.S)
        nt = nt.replace('&nbsp;','')
        nt = nt.strip('.pdf')
        self.nxtitle = nt
    def handle_supind(self):
        pat = r'<span class="m-r-md">适用行业：(.*?)</span>'
        sup_ind = S_search(pat,self.s,re.S)
        self.sup_ind = replace_brac(sup_ind)
       
    
            
    def handle_mbody(self):
        soup = BeautifulSoup(self.s,'lxml')
        mbody = soup.find_all(class_='detail-content')
        
        if len(mbody) == 0:
            print('No Main Body')
            print(self.url)
            self.mbody = ""
            return
        self.mbody = replace_brac(str(mbody[0]))
        
    
    def handle_detail(self):
        self.handle_requests()
        self.handle_source()
        self.handle_money()
        self.handle_nexturl()
        self.handle_mbody()
        self.handle_next_title()
        self.handle_supind()
#         self.handle_appendix()
        
    


# In[5]:


### 文号 正文 附件  ## 适用对象 个人 企业 综合

if __name__ == '__main__':
    url = 'https://www.chacha.top/sup_item?id=6c7b28c7f7b79bdc508b'
#     url = 'https://www.chacha.top/sup_item?id=059f8dd7988e6d0e0b59'
#     url = 'https://www.chacha.top/macro_policy?id=0366481e2dc1572048b7'
    dp = DetailPage(url)
    dp.handle_detail()
#     print(dp.artid)
#     print(dp.appendix)


# In[19]:


# print(dp.source)
# print(dp.money)
# print(dp.mbody)

# print(dp.next_url)

# print(dp.nxtitle)
# print(dp.sup_ind)


# In[17]:


# sentence = HanLP.parseDependency("成都市大邑县企业获得省、市科技奖励资助")
# print(sentence)

# print(getBin(sentence))

# sentence = HanLP.parseDependency("成都市大邑县培育高新技术企业集群")
# print(sentence)

# print(getBin(sentence))


# In[ ]:




