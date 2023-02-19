import datetime 
time_now=datetime.datetime.now()
delta_m1=datetime.timedelta(days=-1)
delta_p1=datetime.timedelta(days=1)
time_yesterday=time_now+delta_m1    
time_tomorrow=time_now+delta_p1
print("Yesterday:",time_yesterday.strftime("%d/%m/%y"))
print("Today:", time_now.strftime("%d/%m/%y"))
print("Tomorrow:",time_tomorrow.strftime("%d/%m/%y"))
