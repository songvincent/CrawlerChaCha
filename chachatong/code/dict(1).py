
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
       
if __name__ == "__main__":
    a=getdeptid("河南省人民政府")
    print(a)
