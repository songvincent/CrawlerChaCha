#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
import time
import re


# In[8]:


### 鼠标移动构建加载更多数据

def MouseDown(browser,num,i):
    
#     i = 3000
    for k in range(num):
#         print(k)
        js = "window.scrollTo(0,{});".format(str(i))
        browser.execute_script(js)
        time.sleep(2)
        i += 3000
    return i


# In[9]:


url = 'https://www.chacha.top/origin?area=true'
path1 = '../sfdrive/geckodriver.exe'
browser = webdriver.Firefox(executable_path = path1)
browser.get(url)
time.sleep(1)


# In[10]:


# browser.get(url)
start = time.clock()
tlength = 0
i = 3000
with open('result.txt','w+',encoding='utf-8') as fout:
    while True:
        i = MouseDown(browser,5,i)  ##10次100条
        time.sleep(2)
        text = browser.page_source

        ## 拿到详情页列表
        pat = r'<ul class="clearfix policy-data">(.*?)</ul>'
        con = re.search(pat,text,re.S)
        con = con.groups()[0]

        lipat = r'<li class="sup-list-item m-b-md".*?data-id="(.*?)" data-type="(.*?)">(.*?)</li>'
        policy_lst = re.findall(lipat,con,re.S)
        length = len(policy_lst)
        fout.write(str(length)+","+str(tlength))
        fout.write('\n')
        print(length,tlength)
        if length <= tlength:
            break
        tlength = length
elapsed = (time.clock() - start)
print("Time used:",elapsed)


# In[ ]:




