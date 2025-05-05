#sytax :objname._classname_privatemethod-------private method
#private method usage
'''
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("from class method,var=",self.__var)
obj=abc(100)
obj._abc__display()
'''

#code to call a class method from another method in the same class
'''
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Variable is :",self.var)
    def add_value(self):
        self.var+=5
        self.display()
obj=abc(10)
obj.add_value()
'''

#class method,which calls a function defined global namespace
'''
def add(x):
    print("Variable is :"+str(x))
class abc():
    def __init__(self,x):
        self.x=x
        x+=5
        add(x)
obj=abc(10)
'''
'''
def add(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
    def modify(self):
        self.var=add(self.var)
        print("var is:",self.var)
obj=abc(10)
obj.display()
obj.modify()
'''

#built-in functions - get ,set ,delete,getattr(),setattr() and deleteattr()
'''
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
obj=abc(10)
obj.display()
print("obj has attribute var ",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',55)
print("After setting value,var is:",obj.var)
setattr(obj,'count',10)
print("new variable count is created with value",obj.count)
print("Before deleting ",obj.var)
delattr(obj,'var')
print("After deleting ",obj.var) #we got an error
'''

#Builtin class attr
#1).__doc__  --when string doc is not specified n return attr
#2).__dict_namespace access attributes
#3).__name__ returns class attr's name
#4).__module__
#5).__bases__ it is used more in inheritance
'''
class abc():
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def display(self):
        print("var1:",self.v1)
        print("var2:",self.v2)
obj=abc(10,12.345)
obj.display()
print("object.__dict__ :",obj.__dict__)
print("object.__doc__ :",obj.__doc__)
print("object.__name__ :",abc.__name__)
print("object.__module__ :",obj.__module__)
print("class.__bases__ :",abc.__bases__)
'''
#program that uses class as student to store name,
#marks of a student,use a list to store the marks of the 3 subjects.
#Constraints:
#1.take class as student
#2.create a constructor for the student name
#3.create a function for marks,to be enteres manually with in the class function and add the marks to the list
#4.display the student name and the marks he/she got
#5.pass the object's attributes of two student names
#TestCases:
#obj1:"vijay"
#obj2:"Ajay"
#Output :vijay got [88,88,90]
#         Anil got [77,78,90]
'''
class student():
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def student_marks(self,l,l1):
        print(self.n1+" got "+str(l))
        print(self.n2+" got "+str(l1))
l=list(map(int,input("ENTER list1:").split(" ")))
l1=list(map(int,input("ENTER list2:").split(" ")))
n1=input("Enter name1:")
n2=input("Enter name2:")
obj=student(n1,n2)
obj.student_marks(l,l1)
'''
'''
class student():
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("enter %s marks in %d subject:" %(self.naem,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
obj1=student("vijay")
obj1=entermarks()
obj2=student("anil")
obj2.entermarks()
obj1.display()
obj2.display()
'''

#program that has a class circle,use a class variable to define the valueof constant pi.
#use this class variable to calculate the area and circumference of circle with specified radius
#constraint:
#pi with the class variable as 3.14159
#radius=7.5
#return the area and circumference values to main program by creating function with the calss respectively

class circle():
    pi=3.14159
    def area(self,r):
        print("The area of circle is:",circle.pi*r*r)
    def circumference(self,r):
        print("The circumference of circle is:",2*circle.pi*r)
obj=circle()
r=float(input("Enter the radius:"))
obj.area(r)
obj.circumference(r)
        
    



#Garbage Collections
#Gabage value--unnessary value























