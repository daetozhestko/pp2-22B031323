from datetime import datetime ,time
def difference_inSeconds(date_2,date_1):
    timedelta=date_2-date_1
    return timedelta.days *24 *3600 + timedelta.seconds
date_1= datetime(2015, 3, 17, 12, 3, 5)
date_2=datetime.now()

print(difference_inSeconds(date_2,date_1),"seconds")

