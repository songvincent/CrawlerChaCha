# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

def get_theme(filename):
    score=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    dic={0:'成果转化',1:'资金扶持',2:'资格资质',3:'人才引育',4:'双创投资',5:'减税降费',6:'市场监管',7:'资源共享',8:'知识产权'}
    di={'奖励':0,'成果':0,'转化':0,
'补贴':0,'补助':0,'金融':0,'贷款':0,'借款':0,'资金':0,'补偿':0,'扶持':0,
'认证':0,'认定':0,'资格':0,'资质':0,'评定':0,
'招聘':0,'人才':0,'人才引进':0,'人才培养':0,
'创业':0,'创新':0,'载体':0,'研发':0,'升级':0,
'减税':0,'降费':0,'税率':0,'国税':0,'地税':0,
'监管':0,'管理':0,
'资源':0,'共享':0,'开放':0,
'知识产权':0,'专利':0,'发明':0,'论文':0,'软件著作权':0,'集成电路专利':0,'研发':0}

    with open(filename, 'r', encoding="gb2312") as f:
        contents=f.read()
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
    if(max_score==0):
        return("其他")
    else:
        for i in range(0,9):
            if score[i]==max_score:
               theme_name.append(dic[i]) 
        return(theme_name)

def get_supportdirection(filename):
    score=[0, 0, 0, 0, 0, 0, 0]
    dic={0:'创新创造',1:'做优做强',2:'拓展发展',3:'企业权益',4:'营商环境',5:'减税降费',6:'解决融资'}
    di={'创业':0,'创新':0,'知识产权':0,'专利':0,'发明':0,'论文':0,'软件著作权':0,'集成电路专利':0,'研发':0,
'优化':0,'奖励':0,'改造':0,'建设':0,'示范':0,'重大':0,'龙头':0,'扶持':0,'补贴':0,'扩大':0,'提升':0,'发展':0,'升级':0,'提速':0,'增效':0,
'扩展':0,'发展':0,'合作':0,'支持':0,'并配':0,'重组':0,
'权益':0,'利益':0,
'营商':0,'环节':0,'建设':0,'楼宇环境':0,
'减税':0,'降费':0,'税率':0,'国税':0,'地税':0,'补偿':0,
'补贴':0,'补助':0,'金融':0,'贷款':0,'借款':0,'资金':0,'信贷':0,'银行':0
}
    
    with open(filename, 'r', encoding="gb2312") as f:
        contents=f.read()
        
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
    if(max_score==0):
        return("其他")
    else:
        for i in range(0,7):
            if score[i]==max_score:
               supportdirection.append(dic[i]) 
        return(supportdirection)

    
    
filename="C:\\Users\\wangzhuoyue\\Desktop\\test.txt"    
themename=get_theme(filename)
supportdirection=get_supportdirection(filename)
print(themename)
print(supportdirection)
