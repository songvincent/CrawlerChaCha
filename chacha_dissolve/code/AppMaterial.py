#!/usr/bin/env python
# coding: utf-8

# In[2]:


from util import *
import requests


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


import pyhanlp
from pyhanlp import *


# In[44]:


class AppMaterial2:
    
    def __init__(self,url):
        
        self.url = url
        self.mbody = ""
        self.material = ""
        
    def getCon(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        r = requests.get(self.url,headers=headers, timeout=6)
        s = r.content.decode('utf-8')  ## decode
        return s
    
    def handleBody(self):
        
        s = self.getCon()
        soup = BeautifulSoup(s,'lxml')
        mbody = soup.find_all(class_='detail-content')
        if len(mbody) == 0:
            print('No Main Body')
            print(self.url)
            mbody = ""
        #     return
        mbody = str(mbody[0])
        self.mbody = mbody
        return mbody
    
    def getSpans(self,title):
        
        sentence = HanLP.parseDependency(title)
        print(sentence)
        tbin = getBin(sentence)
        print(tbin)
        mbody = self.handleBody()
        print(mbody)
        spans = get_inbrac(tbin,mbody)
#         print(mbody)
        print(spans)
        span = spans[0]
        tpan = span[1]-span[0]-len(title)
        if abs(tpan) < 10:
#             print('00000000')
            tn = getNxSpan(mbody,spans[0])
        else:
            tn = spans[0]
        return tn
    
    def handleM(self,title):
        span = self.getSpans(title)
#         print(span)
        self.material = self.mbody[span[0]:span[1]]


# In[45]:


## 本金损失补偿 最后一个为 核心关系
##  机器换人           最后一个为 核心关系 'https://www.chacha.top/sup_policy?id=48371700fab06412c7a0' '天津市支持实施工业企业 “机器换人”工程'
## 改造补助 成都市武侯区楼宇节能环保改造补助 https://www.chacha.top/sup_policy?id=56bf01ea58e52e506f5e


# In[ ]:


class AppMaterial:
    
    def __init__(self,url):
        
        self.url = url
        self.mbody = ""
        self.material = ""
        
    def getCon(self):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        r = requests.get(self.url,headers=headers, timeout=6)
        s = r.content.decode('utf-8')  ## decode
        return s
    
    def handleBody(self):
        
        s = self.getCon()
        soup = BeautifulSoup(s,'lxml')
        mbody = soup.find_all(class_='detail-content')
        if len(mbody) == 0:
            print('No Main Body')
            print(self.url)
            mbody = ""
        #     return
        mbody = str(mbody[0])
        self.mbody = mbody
        return mbody
    
    
    def handleM(self,title):
        mbody = self.handleBody()
        if "申请材料" in mbody:
            print(self.url)
#         print(span)
        self.material = ""


# In[48]:


if __name__ == '__main__':
    
    url = 'https://www.chacha.top/sup_policy?id=56bf01ea58e52e506f5e'
    am = AppMaterial(url)
    title = '成都市武侯区鼓励楼宇参加标准化建设试点奖励'
    am.handleM(title)
    print(am.material)
#     print(material)


# In[43]:


def getBin(sentence): ## 获得宾语
    ### DIR(sentence)
    word_array = sentence.getWordArray()
    length = len(word_array)
    flag = 0
    do = 0
    res = []
    for i in range(length-1,-1,-1):
        word = word_array[i]    ### dir(word)
        lem = word.LEMMA
        dep = word.DEPREL

        if flag == 0 and do != 1:
            if dep == "并列关系" or dep == "标点符号":
                res.insert(0,lem)
            elif dep == "核心关系":
                res.insert(0,lem)
                do = 1
            else:
                flag = 1
            
        if do == 1:
            if dep == '并列关系' or dep == '定中关系' or dep == '标点符号':
                res.insert(0,lem)
            elif dep == "核心关系":
                continue
            else:
                break
        else:
            
            if flag == 1:
                if dep == '动宾关系':
                    res.insert(0,lem)
        #             continue
                else:
                    flag = 2
            if flag == 2:
                if dep == '定中关系':
                    res.insert(0,lem)
                else:
                    break

    return "".join(res)


# In[16]:


# def getNxSpan(mbody,span):
#     length = len(mbody)
#     st = span[1]
#     start = -1
#     end = -1
#     flag = 0
#     for i in range(st,length):
#         if flag == 0:
#             isc = is_Chinese(mbody[i])
#             if isc == True:
#                 flag = 1
#                 start = i
#     #             print(mbody[i])
#         else:
#             if mbody[i] == '<':
#                 end = i
#                 break
                
#     return [start,end]

# def is_Chinese(word):
#     if '\u4e00' <= word <= '\u9fff':
#         return True
#     return False


# In[ ]:




