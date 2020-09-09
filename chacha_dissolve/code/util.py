#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pyhanlp
from pyhanlp import *


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

def replace_brac(text):
    ''' 去除掉<p...></p> <a ...> 等内容
    而如果其中href = 后面的字符串中包含网址是特定网址
    则保留该网址'''
    prefix = 'http://www.gdzwfw.gov.cn'
    urls = re.findall('href="(.*?)"',text)
#     print(urls)
    if len(urls) == 0:
        url = ''
    else:
        url = urls[0]
        if 'gov.cn' in url:
            if url.startswith('http'):
                pass
#                 url = url
            else: ## 图片url = //static.gdzwfw.gov.cn/guide/files/21...
                url = prefix + url
                
        elif url.startswith('http'): ## 点击访问
            url = url
        else:  ## href = javascript()
            url = ''
    text = re.sub('<.*?>','',text)
    if url == '':
        return text
    else:
        return text+"("+url+")"
		
def getBin1(sentence): ## 获得宾语
    ### DIR(sentence)
    word_array = sentence.getWordArray()
    length = len(word_array)
    flag = 0
    res = []
    for i in range(length-1,-1,-1):
        word = word_array[i]    ### dir(word)
        lem = word.LEMMA
        dep = word.DEPREL

        if flag == 0:
            if dep == '动宾关系':
                res.insert(0,lem)
    #             continue
            else:
                flag = 1
        if flag == 1:
            if dep == '定中关系':
                res.insert(0,lem)
            else:
                break


    return "".join(res)

def get_inbrac(obj,mbody):  ## 找到 > < 这两个括号的位置（根据这两个尖括号中的内容）
#     obj = "属地法人注册率"
    citer = re.finditer(obj,mbody,re.S)
    bs = []
    for c in citer:
        span = c.span()
        length = len(mbody)
        sta = span[0]
        end = span[1]

        b1 = [-1,-1]

        for i in range(sta,-1,-1):

            mb = mbody[i]
            if mb == '>':
                b1[0] = i+1

                break

        for j in range(end,length):
            mb = mbody[j]
            if mb == '<':
                b1[1] = j
                break
    #     print(b1)
        bs.append(b1)
    return bs
	
def getBin(sentence): ## 获得宾语
    ### DIR(sentence)
    word_array = sentence.getWordArray()
    length = len(word_array)
    flag = 0
    res = []
    for i in range(length-1,-1,-1):
        word = word_array[i]    ### dir(word)
        lem = word.LEMMA
        dep = word.DEPREL

        if flag == 0:
            if dep == "并列关系" or dep == "标点符号":
                res.insert(0,lem)
            else:
                flag = 1
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
	
def is_Chinese(word):
    if '\u4e00' <= word <= '\u9fff':
        return True
    return False
	
def getNxSpan(mbody,span):
    length = len(mbody)
    st = span[1]
    start = -1
    end = -1
    flag = 0
    for i in range(st,length):
        if flag == 0:
            isc = is_Chinese(mbody[i])
            if isc == True:
                flag = 1
                start = i
    #             print(mbody[i])
        else:
            if mbody[i] == '<':
                end = i
                break
                
    return [start,end]




