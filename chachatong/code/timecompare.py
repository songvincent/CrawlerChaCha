import datetime
import time
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
        

if __name__=='__main__':
    result=timecompare("2020-08-25")   
    print(result) 