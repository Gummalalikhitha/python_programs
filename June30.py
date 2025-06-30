'''
Modules
math
random
datetime
calendar
json  -->  It normalize the data/serializig
.csv
sqlite3 -->It is used to access the database
#Download sqlite3 i.e sql tools and connect mysql to the vsc
os module --> directory operations
collections module
regex -->regular pattern
itertools
'''
#Most common functions in math module
'''
sqrt
factorial
pow
floor
ceil
pi
'''
#math module
'''
import math
n=int(input("Enter"))
print("Square root:",math.sqrt(n))
print("Factorial of n:",math.factorial(n))
print("Pi value:",f'{math.pi:.4f}')
print("Pi operation:","%.2f" % math.pi*2)
'''
#random module
'''
import random
#random -->generate numbers,random choices
a=random.randint(2,9)
print("Random number from 10 to 50:",a)
#for floating numbers in between 0 to 1
print("Random number from 0 to 1:",random.random())
#for floating random number (uniform) 
print("Random number from 1.5 to 5.5",random.uniform(1.5,5.5))
#choice
b=random.choices([1,3,4,5]) #--->It is used to print thechoice value in list
c=random.choice([1,3,4,5])
print("Random choices from a list in list dtype:",b)
print("Random choice from given list:",c)
#shuffle
l=[1,2,3,3,3,2,1,2,4,5]
random.shuffle(l)
print("shuffle list:",l)
#sample --->It also get duplicates in the data
print(random.sample(l,4))
random.seed(80)
print(random.randint(1,100))
'''

#datetime
'''
datetime
datetime.now()
datetime.strptime()
epoch
datetime.strftime
timedelta
date.today()
datetime.date
%I =0-12
%p=AM/PM
%H-0->23.59.59.00000
'''
from datetime import datetime,date,timedelta
#current time and date
now=datetime.now()
print(now)
#only date
print("Todaysdate:",date.today())
#Formatted date and time
formatted=now.strftime("%d-%m-%Y %H:%M:%S") #Y-2025,y-25
print("Formatted datetime:",formatted)
#parsddatetime
date_str="24-12-2000 14:55:00"
parsed=datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")
print("parsed data:",parsed)
#timedelta
tomorrow=now+timedelta(days=1)
yesterday=now-timedelta(days=1)
print("Tomorrow:",tomorrow)
print("Yesterday:",yesterday)
ftime=now+timedelta(hours=3,minutes=30)
print("After 3.5hrs:",ftime)

now=datetime.now()
format_12hr=now.strptime("%d/%m/%Y %I:%M:%s %p")
print(format_12hr)