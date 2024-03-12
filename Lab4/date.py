import datetime

#1 

t1 = datetime.datetime.now()
t2 = datetime.timedelta(days=5)
print(t1 - t2)

#2

yest = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%A")
today = datetime.datetime.now().strftime("%A")
tom = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A")
print(f"Yesterday: {yest} \nToday: {today} \nTomorrow: {tom}")

#3

t = datetime.datetime.now().replace(microsecond=0)
print(t)

#4

t = datetime.datetime.now().replace(microsecond=0)
sec = int(input("second: "))
print(t - datetime.timedelta(seconds=sec))

