#Formatting
'''
def hi(a):
    return f"I am a {a}."
print(hi("student"))
'''
#default parameters
'''
def a(x,y=2):
    return x*y
print(a(5))
print(a(5,3))
'''
#variable arguments
'''
def add(*a):
    s=0
    for i in a:
        s+=i
    return s
print(add(1,2,3,4,5,6,7,8,9))

def add(*a):
    return sum(a)
print(add(1,2,3,4,5,6,7,8,9))
'''
#keyword arguements
'''
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value} ")
info(name="vijay",age=20,city="goa")
'''
#Lambda Function
'''
sqre=lambda x:x*x
add=lambda x,y:x+y
print(add(5,9))
print(sqre(5))
'''
#write a program to return multiple values
#min,max,avg by passing 1,2,3,4,5 to a function
'''
def samp(*a):
    return f"Min :{min(a)},Max :{max(a)},Avg :{sum(a)/len(a)}"
print(samp(1,2,3,4,5))

def values(numbers):
    return min(numbers),max(numbers),sum(numbers)/len(numbers)
min_val,max_val,avg=values([1,2,3,4,5])
print(f"min :{min_val},Max :{max_val},Avg :{avg}")
'''
#Recursion
#1.Direct    2.Indirect                           3.Head/Non-Tail     4.Tail
#5.Linear    6.Binary                             7.Multiple                8.Nested
#9.Mutual   10.Divide_&_Conquer     11.Tree                   12.Absolute/Static

#Recursive fact
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''
#Recursive even or odd
'''
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
print(is_even(4))
print(is_odd(7))
'''
#create a program to determine if a string is a palindrome by recursively comparing characters from start to end by base case function
#and call if the pointer meets its palindrome
#Constraints:
'''
def is_palindrome length
def check_palindrome start,end,s

input:
racecar=True
hello=Fasle
level=True
'''
'''
def is_palindrome(n):
    if len(n)<2:
        return False
    i=0
    j=len(n)-1
    while(i<=j and n[i]==n[j]):
        i+=1
        j-=1
        return True
    return False
print(is_palindrome("moderm"))
'''
'''        
def is_p(s):
    if len(s)<=1:
        return True
    return check_p(s,0,len(s)-1)
def check_p(s,start,end):
    if start>=end:
        return True
    if s[start] !=s[end]:
        return False
    return is_p(s[start+1:end])
print(is_p("racecar"))
print(is_p("hello"))
print(is_p("madaem"))

def ftail(n,acc=1):
    if n==0 or n==1:
        return acc
    return ftail(n-1,n*acc)
print(ftail(5))

def ackerman(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackerman(m-1,1)
    else:
        return ackerman(m-1,ackerman(m,n-1))
print(ackerman(2,1))

def func(n):
    if n>50:
        return n-5
    else:
        return func(n+5)
print(func(30))
'''
#Superfactorial
'''
def fact(n):
    if n==0 or n==1:
        return  1
    return n*fact(n-1)
def super_fact(n):
    p=1
    for i in range(1,n+1):
        p*=fact(i)
    return p
print(super_fact(5))
        
def sfact(n):
    if n<=0:
        return 1
    return fact(n)*sfact(n-1)
def fact(n):
    if n<=1:
        return  1
    return n*fact(n-1)
print(sfact(5))
'''
#Power Tower---nested recursion
def pt(a,n):
    if n==1:
        return a
    return a**pt(a,n-1)
print(pt(2,3))
print(pt(3,2))


    



