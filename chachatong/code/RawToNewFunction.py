#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json

import os
import re


# In[2]:


import pyhanlp
from pyhanlp import *


# In[5]:


import datetime
import time


# In[3]:


## 得到主题分类
def get_theme(contents):
    score=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    dic={0:'ZTBM001',1:'ZTBM002',2:'ZTBM003',3:'ZTBM004',4:'ZTBM005',5:'ZTBM006',6:'ZTBM007',7:'ZTBM008',8:'ZTBM009'}
    #dic={0:'成果转化',1:'资金扶持',2:'资格资质',3:'人才引育',4:'双创投资',5:'减税降费',6:'市场监管',7:'资源共享',8:'知识产权'}
    di={'奖励':0,'成果':0,'转化':0,
'补贴':0,'补助':0,'金融':0,'贷款':0,'借款':0,'资金':0,'补偿':0,'扶持':0,
'认证':0,'认定':0,'资格':0,'资质':0,'评定':0,
'招聘':0,'人才':0,'人才引进':0,'人才培养':0,
'创业':0,'创新':0,'载体':0,'研发':0,'升级':0,
'减税':0,'降费':0,'税率':0,'国税':0,'地税':0,
'监管':0,'管理':0,
'资源':0,'共享':0,'开放':0,
'知识产权':0,'专利':0,'发明':0,'论文':0,'软件著作权':0,'集成电路专利':0,'研发':0}

#     with open(filename, 'r', encoding="gb2312") as f:
#         contents=f.read()
    di['奖励']=contents.count('奖励')
    di['成果']=contents.count('成果')
    di['转化']=contents.count('转化')
    
    di['补贴']=contents.count('补贴')
    di['补助']=contents.count('补助')
    di['金融']=contents.count('金融')
    di['贷款']=contents.count('贷款')
    di['借款']=contents.count('借款')
    di['资金']=contents.count('资金')
    di['补偿']=contents.count('补偿')
    di['扶持']=contents.count('扶持')
    
    di['认证']=contents.count('认证')
    di['认定']=contents.count('认定')
    di['资格']=contents.count('资格')
    di['资质']=contents.count('资质')
    di['评定']=contents.count('评定')
    
    di['招聘']=contents.count('招聘')
    di['人才']=contents.count('人才')
    di['人才引进']=contents.count('人才引进')
    di['人才培养']=contents.count('人才培养')
    di['人才']=di['人才']-di['人才引进']-di['人才培养']
    
    di['创业']=contents.count('创业')
    di['创新']=contents.count('创新')
    di['载体']=contents.count('载体')
    di['研发']=contents.count('研发')
    di['升级']=contents.count('升级')
    
    di['减税']=contents.count('减税')
    di['降费']=contents.count('降费')
    di['税率']=contents.count('税率')
    di['国税']=contents.count('国税')
    di['地税']=contents.count('地税')
    
    di['监管']=contents.count('监管')
    di['管理']=contents.count('管理')
    
    di['资源']=contents.count('资源')
    di['共享']=contents.count('共享')
    di['开放']=contents.count('开放')
    
    di['知识产权']=contents.count('知识产权')
    di['专利']=contents.count('专利')
    di['发明']=contents.count('发明')
    di['论文']=contents.count('论文')
    di['软件著作权']=contents.count('软件著作权')
    di['集成电路专利']=contents.count('集成电路专利')
    di['研发']=contents.count('研发')
    
    score[0]=di['奖励']+di['成果']+di['转化']
    score[1]=di['补贴']+di['补助']+di['金融']+di['贷款']+di['借款']+di['资金']+di['补偿']+di['扶持']
    score[2]=di['认证']+di['认定']+di['资格']+di['资质']+di['评定']   
    score[3]=di['招聘']+di['人才']+di['人才引进']+di['人才培养']
    score[4]=di['创业']+di['创新']+di['载体']+di['研发']+di['升级']
    score[5]=di['减税']+di['降费']+di['税率']+di['国税']+di['地税']
    score[6]=di['监管']+di['管理']
    score[7]=di['资源']+di['共享']+di['开放']
    score[8]=di['知识产权']+di['专利']+di['发明']+di['论文']+di['软件著作权']+di['集成电路专利']+di['研发']
    #print(score) 有相等的
    max_score=max(score)
    theme_name=[]
    if max_score==0:
        return ["ZTBM010"]
    else:
        for i in range(0,9):
            if score[i]==max_score:
                theme_name.append(dic[i]) 
        return theme_name


# In[4]:


### 得到扶持方向
def get_supportdirection(contents):
    score=[0, 0, 0, 0, 0, 0, 0]
    dic={0:'FCFX001',1:'FCFX002',2:'FCFX003',3:'FCFX004',4:'FCFX005',5:'FCFX006',6:'FCFX007'}
    #dic={0:'创新创造',1:'做优做强',2:'拓展发展',3:'企业权益',4:'营商环境',5:'减税降费',6:'解决融资'}
    di={'创业':0,'创新':0,'知识产权':0,'专利':0,'发明':0,'论文':0,'软件著作权':0,'集成电路专利':0,'研发':0,
'优化':0,'奖励':0,'改造':0,'建设':0,'示范':0,'重大':0,'龙头':0,'扶持':0,'补贴':0,'扩大':0,'提升':0,'发展':0,'升级':0,'提速':0,'增效':0,
'扩展':0,'发展':0,'合作':0,'支持':0,'并配':0,'重组':0,
'权益':0,'利益':0,
'营商':0,'环节':0,'建设':0,'楼宇环境':0,
'减税':0,'降费':0,'税率':0,'国税':0,'地税':0,'补偿':0,
'补贴':0,'补助':0,'金融':0,'贷款':0,'借款':0,'资金':0,'信贷':0,'银行':0
}
    
#     with open(filename, 'r', encoding="gb2312") as f:
#         contents=f.read()
        
    for k,v in di.items():
        di[k]=contents.count(k)
    
    score[0]=di['创业']+di['创新']+di['知识产权']+di['专利']+di['发明']+di['论文']+di['软件著作权']+di['集成电路专利']+di['研发']
    score[1]=di['优化']+di['奖励']+di['改造']+di['建设']+di['示范']+di['重大']+di['龙头']+di['扶持']+di['补贴']+di['扩大']+di['提升']+di['发展']+di['升级']+di['提速']+di['增效']
    score[2]=di['扩展']+di['发展']+di['合作']+di['支持']+di['并配']+di['重组']
    score[3]=di['权益']+di['利益']
    score[4]=di['营商']+di['环节']+di['建设']+di['楼宇环境']
    score[5]=di['减税']+di['降费']+di['税率']+di['国税']+di['地税']+di['补偿']
    score[6]=di['补贴']+di['补助']+di['金融']+di['贷款']+di['借款']+di['资金']+di['信贷']+di['银行']
    #print(score) #有相等的
    max_score=max(score)
    supportdirection=[]
    if max_score==0:
        return ["FCFX008"]
    else:
        for i in range(0,7):
            if score[i]==max_score:
                supportdirection.append(dic[i]) 
        return supportdirection


# In[3]:


def get_agent(rd):
#     rd = rawdata[56]

    con = rd['mainbody']
    con1 = re.sub('<.*?>','',con)  ### 去掉<>中的内容

    word_pos = HanLP.segment(con1) ## hanlp进行分词以及词性标注
#     print(word_pos)
    words = []
    poss = []
    for wp in word_pos:
        wlst = str(wp).split('/')
        words.append(wlst[0])
        poss.append(wlst[1])

    length = len(words)
    agent = []
    agent_nto = []
    agent_all = []
    for i in range(length):
        word = words[i]
        pos = poss[i]

        if pos == 'nto':
            agent_nto.append(word)
            agent_all.append(word)

        elif pos == 'nt':
            agent.append(word)
            agent_all.append(word)
        elif pos == 'nis':
            j = i
            flag = 0
    #         print(j)
            while(j>0 and j>=(i-9)):
                if words[j].strip() == '' or words[j].strip() == '。' or words[j].strip() == '、':
                    break

                if poss[j] == 'ns' and poss[j-1] !='ns':
                    flag = 1
                    break
                j -= 1

            if flag == 1:
                res = ''
                for k in range(j,i+1):
                    res += words[k]
                agent.append(res)
                agent_all.append(res)
    return agent,agent_nto,agent_all


# In[4]:


def get_dept(agent,agent_nto,agent_all):
    
    if len(agent_all) == 1:
        if agent_all[0].endswith('学院'):
            return ""
        return agent_all[0]
    elif len(agent_all)==0:
        return ""
    else:
        
        for i in range(3):
            if i+1 > len(agent_all):
                break
#             print(agent_all[i])
            if (agent_all[i].endswith('人民政府') or agent_all[i].endswith('人民政府办公厅')) and '）' not in agent_all[i] and len(agent_all[i]) > 5:
                return agent_all[i]
            
        if (agent_all[-1].endswith('局') or agent_all[-1].endswith('厅') or agent_all[-1].endswith('政府')) and len(agent_all[-1])>5 and '，' not in agent_all[-1] :
            return agent_all[-1]
        
        res = ""
        rlst = []
        for ag in agent_all:
            rlst.append(ag)
            if ag in rlst:
                continue
            if ag.endswith('局') and len(ag) > 5:
                res = res + ag + ','
        res = res[:-1]
        return res


# In[ ]:


def getdeptid(dept):
    flag=0
    if (dept.find("国务院办公厅")>=0 or dept.find("政府")>=0): 
        flag=1
        return 'BMZ005'
    if (dept.find("经信")>=0 or dept.find("工业和信息化")>=0 or dept.find("经济和信息化")>=0):
        flag=1
        return 'BMZ006'  
    if (dept.find("财政")>=0): 
        flag=1
        return 'BMZ007'  
    if (dept.find("发改")>=0 or dept.find("发展和改革")>=0):
        flag=1
        return 'BMZ008'
    if (dept.find("农业")>=0):
        flag=1
        return 'BMZ009'        
    if (dept.find("商务")>=0):
        flag=1
        return 'BMZ010' 
    if (dept.find("市场监督管理")>=0):
        flag=1
        return 'BMZ011'
    if (dept.find("金融")>=0 or dept.find("中国人民银行")>=0 or dept.find("中国银行保险监督管理委员会")>=0 or dept.find("中国证券监督管理委员会")>=0):
        flag=1
        return 'BMZ012'
    if (dept.find("国际贸易促进委员会")>=0):
        flag=1
        return 'BMZ013'    
    if (dept.find("人社")>=0 or dept.find("人力资源")>=0):
        flag=1
        return 'BMZ014'    
    if (dept.find("工商业联合")>=0):
        flag=1
        return 'BMZ015'  
    if (flag==0):
        return 'BMZ016'   


# In[9]:


def timecompare(timestr):
    #获取当前时间日期
    nowTime_str = datetime.datetime.now().strftime('%Y-%m-%d') 
    #mktime参数为struc_time,将日期转化为秒，
    e_time = time.mktime(time.strptime(nowTime_str,"%Y-%m-%d"))
    s_time = time.mktime(time.strptime(timestr, '%Y-%m-%d'))
    #日期转化为int比较
    diff = int(s_time)-int(e_time)
    if diff > 0:#当前时间在给定时间之前 返回-1
        return -1
    if diff==0:
        return 0
    if diff<0:#当前时间在给定时间之后 返回1
        return 1


# In[15]:


# level = {"国家级": "BMZ001", "省级": "BMZ002", "市级": "BMZ003", "区县级": "BMZ004"}
# lvl = ["国家级","省级","市级","区县级"]
def get_level(area):
    lvl = ["国家级","省级","市级","区县级"]
    level = {"国家级": "BMZ001", "省级": "BMZ002", "市级": "BMZ003", "区县级": "BMZ004"}
    sym = area[-1]
#     print(rd['area'])
#     print(sym)
    for v in lvl:
        if sym in v:
            return level[v]
    return 'BMZ000'


# In[16]:


## 得到 有效标识
def get_validflag(timespan):
    if len(timespan) == 0:
        return 1
    else:
        t1 = timecompare(timespan[0].strip())
        if t1 == 1 or t1 == 0:
            if timespan[1] == -1:
                return 1
            else:
                t2 = timecompare(timespan[1].strip())
                if t2 == -1 or t2 == 0:
                    return 1
                else:
                    return 0
        else:
            return 0


# In[ ]:


## 处理适用对象
## ## 除了标题中包括：人才认定、人才评定为个人外，其他的都设置为企业
def get_tcode(title):
    if '人才认定' in title or '人才评价' in title:
        return 'BMZ018' ## 人才
    else:
        return 'BMZ017' ## 企业


# In[ ]:


### 处理发布时间与时间周期
def get_vdata(ttime,tspan):
    res1 = ""
    res2 = ""
    res3 = ""
    if ttime == "" :
        res1 =  '0000-00-00'
    
    else:
        res1 = ttime
    
    if len(tspan) == 0:
        res2 = '0000-00-00'
        res3 = '0000-00-00'
    else:
        res2 = tspan[0]
        if tspan[1] == -1:
            res3 = '0000-00-00'
        else:
            res3 = tspan[1]
    return res1,res2,res3


# In[6]:


if __name__ == '__main__':
    path = "../data/"
    filename = 'result.json'
    with open(path+filename,'r',encoding='utf-8') as fin:
        rawdata = json.load(fin)
    fin.close()


# In[10]:


# rd = rawdata[15]

# rd.keys()


# print(get_supportdirection(rd['title']+rd['mainbody']))
# print(get_theme(rd['title']+rd['mainbody']))


# In[8]:


# with open('agent.txt','w+',encoding='utf-8') as fout:
#     for i in range(len(rawdata)):
#         rd = rawdata[i]
#         dept1 = rd['agent']
#         if '其他' not in dept1:
#             print(i)
#             print(dept1)
#             print(rd['url'])
#             fout.write(dept1+'\n')
#             continue
#         agent,agent_nto,agent_all = get_agent(rd)
#         dept = get_dept(agent,agent_nto,agent_all)
#         print(i)
#         print(dept)
#         print(rd['url'])
#         fout.write(dept+'\n')


# In[14]:


# timecompare('2020-08-20')


# In[ ]:




