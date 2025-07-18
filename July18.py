'''Lambda Functions'''

# data=[10,"hi",4.5,"studnts",3,100]
# from the list containing numbers and strings,extract only integersusing lambda function and list comprehension 
# o/p:[10,3,100]

# a=lambda x:x.isdigit()
# l=input().split(" ")
# b=[i for i in l if a(i)]
# print(b)


# l=[10,'likky',5.4,'gdgdg',80]
# b=[i for i in l if (lambda a:type(a)==int)(i)]
# print(b)

# calculate the factorial o n uing recursion o lambda function n=4
# l=int(input())
# fact=(lambda f:lambda n:1 if n==0 else n*f(f)(n-1))(lambda f: lambda n:1 if n==0 else n*f(f)(n-1))
# print(fact(l))

#sum of digits
# n=int(input())
# nsum=(lambda f:lambda n:0 if n==0 else n%10+f(f)(n//10))(lambda f:lambda n:0 if n==0 else n%10+f(f)(n//10))
# print(nsum(n))

''' lambda function syntax '''
''' pvar=lambda v1,v2 : operation/boolean expression '''
# x=lambda num:num+22
# print(x(3))               # function calling i.e functioname(parametername)

# add=lambda a,b: a+b
# print_=lambda a,b :a if a>b else b 
# print(add(4,5))
# print(print_(2,3))

# num=[11,22,33,44,55,66,77]
# e=list(filter(lambda num :num%2!=0,num))
# e=list(map(lambda num :num%2!=0,num))
# print(e)
# packs=[(1,99),(2,11),(66,66)]
# result=sorted(packs,key=lambda x:x[1])
# print(result)

# def b(n):
#     return lambda x:x**n
# a=b(2)
# print(a(5))  #O/P :25

# def a(n):
#     return n**3
# b=lambda x:x**3
# print(a(2))
# print(b(3))  #O/P :8 \n 27

''' code to declare the longest string using lambda '''

# long=lambda a,b:a if len(a)>len(b) else b
# print(long("Gummala","Likhitha"))
# print(long("1234","12"))

#LC with lambda
# data=['Pen','cAp','baT']
# upper=[(lambda x:x.upper())(i) for i in data]
# lower=[(lambda x:x.lower())(i) for i in data]
# print(upper)
# print(lower)

#lc with lambda to reverse of a string
# a=input()
# print("".join([i for i in (lambda x:x[::-1])(a)]))

#reversing a string with using map,lambda functions
# n=input()
# print("".join(map(lambda x:x,(lambda x:x[::-1])(n))))

'''map function syntax'''
#map(function,iterable)
# function means it can be lambda or normal function 
# iterable means it can be a indexed datatpe such as list,dict,tuple,string,set


# words=["likky","vinee","anu","pandu"]
# rw=[(lambda w:w[::-1])(i) for i in words]
# print(rw)

#lc with lambda function to avoid voi9d spaces string
# words=['hi'," ",'students',"   ","bye","    "]
# remove_spaces=[i for i in [(lambda x:x.strip())(i) for i in words] if i!=""]
# print(remove_spaces)

#lc with lambda function to avoid voi9d spaces string in single list comprehension
words=['hi','  ','likky',"   ",' ',"anu","   "]
remove_spaces=[(lambda x:x.strip())(i) for i in words if (lambda x:x.strip())(i)!=""]
print(remove_spaces)