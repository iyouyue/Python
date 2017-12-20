import time
just_now = time.mktime(time.strptime('2013-11-11 20:30:00','%Y-%m-%d %H:%M:%S'))
now = time.mktime(time.strptime('2017-11-11 20:30:00','%Y-%m-%d %H:%M:%S'))
difference = now-just_now
tuple_time=time.gmtime(difference)

print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(tuple_time.tm_year-1970,tuple_time.tm_mon-1,
											tuple_time.tm_mday-1,tuple_time.tm_hour,
											tuple_time.tm_min,tuple_time.tm_sec))
