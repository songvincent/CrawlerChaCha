import pandas as pd


def excel_one_line_to_list():
    df = pd.read_excel("C:\\Users\\wangzhuoyue\\Desktop\\a.xlsx", usecols=[0],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result0 = []
    for s_li in df_li:
        result0.append(s_li[0])
    print(result0)
    
    
    df = pd.read_excel("C:\\Users\\wangzhuoyue\\Desktop\\a.xlsx", usecols=[1],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result1 = []
    for s_li in df_li:
        result1.append(s_li[0])
    print(result1)
    
    df = pd.read_excel("C:\\Users\\wangzhuoyue\\Desktop\\a.xlsx", usecols=[2],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result2 = []
    for s_li in df_li:
        result2.append(s_li[0])
    print(result2)
    
    df = pd.read_excel("C:\\Users\\wangzhuoyue\\Desktop\\a.xlsx", usecols=[3],
                       names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result3 = []
    for s_li in df_li:
        result3.append(s_li[0])
    print(result3)
    
    dic1={}
    dic2={}
    dic3={}
    
    for i in range(0,19):
        dic1[result3[i]]=result0[i]
        dic2[result3[i]]=result1[i]
        dic3[result3[i]]=result2[i]
    print(dic1)
    print(dic2)    
    print(dic3)
    
if __name__ == '__main__':
    excel_one_line_to_list()