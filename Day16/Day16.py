from datetime import datetime
now = datetime.now()
print(now)
now_string = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now_string)

today = '5 December, 2019'
dateObject = datetime.strptime(today, '%d %B, %Y')
print(dateObject)


t1 = datetime.now()
t2 = datetime(year = 2027, month = 1, day = 1, hour = 0, minute = 0, second = 0)
print(t2 - t1)
t3 = datetime(year=1970, month= 1, day= 1)
print(t1 - t3)