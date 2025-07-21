'''(a+b)*c expression lambda evaluation and returns to another lambda'''
# num1=int(input("Enter value of a:"))
# num2=int(input("Enter value of b:"))
# num3=int(input("Enter value of c:"))
# l1=lambda num1,num2:num1+num2
# l2=lambda value,num3:value*num3
# value=l1(num1,num2)
# value2=l2(value,num3)
# print(value2)

# l2=lambda a:lambda b,c:(a+b)*c
# l1=l2(2)
# value=l1(1,3)
# print(value)

# print((lambda c:lambda a,b:(a+b)*c)(1)(2,3))

'''(a+b)*(c+d)'''
# print((lambda a:lambda b:lambda c,d:(a+b)*(c+d))(2)(3)(4,5))
# print((lambda a,b:lambda c,d:(a+b)*(c+d))(2,3)(4,5))
# print((lambda a,b,c,d:(a+b)*(c+d))(1,2,3,4))

'''(a-b)/(c-d)'''
# try:
#     print((lambda a,b,c,d:(a-b)/(c-d))(1,2,3,4))
# except ZeroDivisionError:
#     print("Denominator subtraction should not be zero")
# except TypeError:
#     print("Invalid Datatype!!!")
'''
assign =op(num)
print(assign(numsquare))
'''
# num=int(input("a:"))
# n=int(input("x:"))
# oper=lambda a:lambda x:(x+a)**2
# numsq=oper(num)   
# print(numsq(n))

'''simple nested lambda string combining with seperator operation for '''
# o=((lambda a:lambda b:lambda c,d:a+"-"+b+"-"+c+"-"+d)("Hi")("Everone")("Good","Morning"))
# print(o)

'''given attributes a,b,c,d are hi,!,students,!!!
write a nested lambda to concatenate the abcd,by converting a and c to uppercase
output:HI!STUDENTS!!!'''
# print((lambda a:lambda c:lambda b,d:a.upper()+b+c.upper()+d)("hi")("students")("!","!!!"))

# a,b,c,d=map(str,input().split(" "))
# print((lambda a:lambda c:lambda b,d:a.upper()+b+c.upper()+d)(a)(c)(b,d))

'''
given attributes a,b,cd are hi,hello,students,teachers !!! 
write a nested lambda to cancatenate the abcd,by reversing with sep ' '
'''
# a,b,c,d=map(str,input().split(" "))
# print(((lambda a:lambda c:lambda b,d:a.upper()+" "+b+" "+c.upper()+" "+d)(a[::-1])(c[::-1])(b[::-1],d[::-1])))
# print(*(lambda a:lambda b:lambda c,d:(a.upper()[::-1],b[::-1],c.upper()[::-1],d[::-1]))(a)(b)(c,d),sep=" ")

''' Transform and Filter'''
# l1=list(map(str,input().split(" ")))
# print([i for i in l1 if (lambda x:len(x)%2==0)(i)])

# numbers=lambda x:lambda a:a*2 if a>x else a*3
# aboe_5=numbers(5)
# num=[4,6,3,8]
# o=list(map(aboe_5,num))
# print(o)

