#class members using class object
'''
class abc():
    var=100
    def display(self):
        print("This is a class method")
    def show(self):
        return self.var+50
obj=abc()
print(obj.var)
obj.display()
print(obj.show())
'''
#class constructor __init__(method)
#-------self is a default parameter and it is used to give access the parameters
#------This constructor is used to automatically initializes the object task in class without
'''
class abc():
    def __init__(self,val):
        print("This is a class method")
        self.val=val
        print("The value is :",val)
    def hello(self,val):
        print("This is a class method")
        self.val=val
        print("The value is :",val)
obj=abc(25)
#obj.__init__(60)
obj.hello(70)
'''
'''
class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("Object var:",var)
        print("Class var:",abc.cv)
obj=abc(10)
obj=abc(35)
'''
#write a program to check whether even or odd
'''
class abc:
    def __init__(self,num):
        self.num=num
        if num%2!=0:
            print(num," is a Odd number")
        else:
            print(num," is a Even number")
obj=abc(45)
obj=abc(78)
a=int(input())
obj=abc(a)
'''
'''
class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def eo(self,num):
        self.check(num)
        if self.even==1:
            print(num," is a even number")
        else:
            print(num," is a odd number")
n=number()
n.eo(23)
'''
#prime number or not
'''
class abc:
    def is_prime(self,num):
        self.num=num
        if num<2:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True
obj=abc()
print(obj.is_prime(172))
'''
#segregate the even and odd parameters in a list and print even list and odd list seperately using a class "number"
'''
class number:
    even=0
    even_list=[]
    odd_list=[]
    def check(self,num):
        if num%2==0:
            self.even=1
    def eo(self,num):
        self.check(num)
        if self.even==1:
            number.even_list.append(num)
            self.even=0
        else:
            number.odd_list.append(num)
    def seperate_list(self,l):
        self.l=l
        for i in l:
            self.eo(i)
        print(number.even_list)
        print(number.odd_list)
n=number()
n.seperate_list([2,1,4,3,7,6,8])
'''
'''
class number:
    even=0
    even_list=[]
    odd_list=[]
    def check(self,num):
        if num%2==0:
            self.even=1
    def eo(self,l):
        self.l=l
        for i in l:
            self.check(i)
            if self.even==1:
                number.even_list.append(i)
                self.even=0
            else:
                number.odd_list.append(i)
        print(number.even_list)
        print(number.odd_list)
n=number()
n.eo([2,1,4,3,7,6,8])
'''
'''
class abc:
    el=[]
    ol=[]
    def __init__(self,l):
        self.l=l
        print("The given list is:",l)
        for i in l:
            if i%2!=0:
                abc.el.append(i)
            else:
                abc.ol.append(i)
        print("The even list is:",abc.el)
        print("The odd list is:",abc.ol)
obj=abc([1,2,3,4,5,6,7,8])
'''
#Class constructor using __del__
'''
class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("Object var:",var)
        print("Class var:",abc.cv)
    def __del__(self):
        abc.cv-=1
        print("Object with %d is going out of scope "%self.var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)
del obj1
del obj3
print(obj2.var)
print(obj3.var)
'''

#Class members using class obj
#__repr__    returns string representation
#__cmp__    2 class obj
#__len__    returns len of obj
'''
class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,object):
        return self.var-object.var
obj=abc("abcdef",41)
print("The value stored in object is :",repr(obj))
print("The length of the name stored in object:",len(obj))
obj1=abc("ghisdkjgjk",1000)
val=obj.__cmp__(obj1)
if val==0:
    print("Both values are equal")
elif val<0:
    print("First value is less than")
else:
    print("Second value is less than first")
'''
#1.__call__()-----instance can be directly called
#2.__lt__(),__le__(),__gt__(),__ge__(),__eq__(),__ne__()
#3.__hash__()-----decide obj/set/dict
#4.__iter__()
#5.__getitem__(),__setitem__()
    
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist)
numlist[3]=10
print(numlist.mylist)
        
        
