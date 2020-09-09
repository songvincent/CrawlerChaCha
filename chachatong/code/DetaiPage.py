#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import re
from util import *
import requests


# In[14]:


from bs4 import BeautifulSoup


# In[67]:


class DetailPage:
    
    def __init__(self,url):
        self.artid = ""
        self.mbody = ""
        self.appendix = []
        
        self.url = url
        self.s = ""
    
    def handle_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        r = requests.get(self.url,headers=headers, timeout=6)
        s = r.content.decode('utf-8')  ## decode
        self.s = s
    
    def handle_artid(self):
        pat = '<span class="m-l-md">文号(.*?)</span>'
        artid = S_search(pat,self.s,re.S)
        if artid.strip() == "":
            print('No artid')
            print(self.url)
            self.artid = ""
        else:
            self.artid = '文号'+artid
            
    def handle_mbody(self):
        soup = BeautifulSoup(self.s,'lxml')
        mbody = soup.find_all(class_='detail-content')
        if mbody == 0:
            print('No Main Body')
            print(self.url)
            self.mbody = ""
            return
        self.mbody = str(mbody[0])
        
    def handle_appendix(self):
        appendix = S_search(r'"file":(.*?)"history"',self.s,re.S)
#         print(appendix)
        if appendix == '[],':
            print('No Appendix')
            print(self.url)
            self.appendix = []
            return
        alst = eval(appendix[:-1])
        
#         print(alst)
        for a in alst:
            b = {}
            b['name'] = a['name']
            b['url'] = 'http:'+a['save_url']
            self.appendix.append(b)
    
    def handle_detail(self):
        self.handle_requests()
        self.handle_artid()
        self.handle_mbody()
        self.handle_appendix()
        
    


# In[68]:


### 文号 正文 附件  ## 适用对象 个人 企业 综合

if __name__ == '__main__':
    url = 'https://www.chacha.top/imple_regu?id=498c2401eac37f63345d'
#     url = 'https://www.chacha.top/macro_policy?id=0366481e2dc1572048b7'
    dp = DetailPage(url)
    dp.handle_detail()
    print(dp.artid)
    print(dp.appendix)


# In[ ]:





# In[ ]:





# In[ ]:




