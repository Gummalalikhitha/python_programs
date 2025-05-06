#Oops
#Multilevel,Multiple,Hierarchy,Hybrid,Multipath

#Multiple inheritance
'''
class base1(object):
    def __init__(self):
        super(base1,self).__init__()
        print("Base Class-1")
class base2(object):
    def __init__(self):
        super(base2,self).__init__()
        print("Base Class-2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("Derived class from both classes")
d=derived()
'''
#initalise classes addition,multiplication in a calculator
#pass the values from main program to the superclass,
#where the subclasses addition and multiplication were triggered
#and return the outputs respectively
#1.take derived class calc
#2.from derived class call subclasses add and null
#3.return the values after math to the object
#4.manual values of both numbers considered within the object
'''
class addition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x+y)
class multiplication:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print(x*y)
class calc(addition,multiplication):
    def __init__(self,x,y):
        addition.__init__(self,x,y)
        multiplication.__init__(self,x,y)
        print("calc class from both classes")
calculator=calc(2,3)
'''
'''
class addition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
class multiplication:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def multiply(self):
        return self.x*self.y
class calc(addition,multiplication):
    def __init__(self,x,y):
        addition.__init__(self,x,y)
        multiplication.__init__(self,x,y)
a=int(input("Enter value x :"))
b=int(input("Enter value y :"))
c=calc(a,b)
print("Sum :",c.add())
print("Product :",c.multiply())
'''
'''
class sqre:
    def __init__(self,x):
        self.x=x
    def square(self):
        return self.x*self.x
class cub:
    def __init__(self,x):
        self.x=x
    def cube(self):
        return self.x*self.x*self.x
class res(sqre,cub):
    def __init__(self,x):
        sqre.__init__(self,x)
        cub.__init__(self,x)
z=int(input("Enter value for a:"))
r=res(z)
print("Square :",r.square())
print("Cube :",r.cube())
print("Their sum is :",r.square()+r.cube())
'''

#multi-level inheritance
'''
class person:
    def name(self):
        print('name.....')
class teacher(person):
    def qualification(self):
        print('Phd')
class hod(teacher):
    def exp(self):
        print("experience 15 yrs.......")
h=hod()
h.name()
h.qualification()
h.exp()
'''
'''
class num:
    def __init__(self,n):
        self.n=n
        print("Number initialized")
class sq(num):
    def square(self):
        return self.n**2
class cu(sq):
    def cube(self):
        return self.n**3
calc=cu(4)
print("square :",calc.square())
print("cube :",calc.cube())
'''    
#Hierarchy inheritance
'''
class number:
    def __init__(self,num):
        self.num=num
    def get_number(self):
        return self.num
class double(number):
    def result(self):
        return self.get_number()*2
class triple(number):
    def result(self):
        return self.get_number()*3
d=double(4)
print("double :",d.result())
t=triple(4)
print("triple :",t.result())
'''
#composition  ,containership -----these two are complex objects

#Abstraction class
class fruit:
    def taste(self):
        raise NotImplementedError()
    def vitamin(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def vitamin(self):
        return "vitamin-A"
    def colour(self):
        return "Yellow"
class orange(fruit):
    def taste(self):
        return "sour and sweet"
    def vitamin(self):
        return "vitamin-C"
    def colour(self):
        return "Orange"
Alphanso=mango()
print(Alphanso.taste(),Alphanso.vitamin(),Alphanso.colour())
org=orange()
print(org.taste(),org.vitamin(),org.colour())

    




















