'''Error and exception
Types o error /exceptions
try - block
except
finally
raising exception
built-in functions '''

'''
5/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    5/0
'''
#ZeroDivisionError: division by zero
'''
v+10
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    v+10
'''
#NameError: name 'v' is not defined
'''
'likky'+3
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    'likky'+3
'''
#TypeError: can only concatenate str (not "int") to str

#Handling zero division error
'''
n=int(input("Enter a numerator:"))
d=int(input("Enter adenominator:"))
try:
    quo=n/d
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator cannot be Zero")
'''

#Multiple Exception Handling
'''
try:
    num=int(input())
    print(num**2)
except (KeyboardInterrupt):
    print("You have to enter a number....not string")
except (ValueError):
    print("Please check before you enter... program end")
print("Bye...!!!")
'''

#Multiple exception in a single block handling
'''
try:
    n=int(input())
    print(n**2)
except (KeyboardInterrupt,ValueError,TypeError):
    print("Please check before entering... program end")
'''
#raise an exception
'''
try:
    n=4
    print(n)
    raise ValueError
except:
    print("even exceuting perfectly... exception raised manually")
'''
#re-=raise error
'''
try:
    raise NameError
except :
    print("re-raise")
    raise
'''
#instance using in exceptions
'''
try:
    raise Exception('hi','students')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    x,y=errorObj.args
    print("Assigned1:",x)
    print("Assigned2:",y)
'''
'''
def div(n,d):
    try:
        quo=n/d
        return quo
    except ZeroDivisionError:
        return "Non-processed"      
n=int(input("Enter a numerator:"))
d=int(input("Enter adenominator:"))
print(div(n,d))
'''
#In-build Excption
#Exception- base class/all exceptions
#SystemExit- sys.exit()
#StandardError-except sys.exit()/stopIteration
#OverflowError-numeric type errors exceeds limit
#Arithmetic -base class or all calci

#basic string contructor
'''
class myError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
try:
    raise myError(99)
except myError as e:
    print("returned string is:",e.value)
    print(type(e.value))
'''
#finally
'''
try:
    print('raise exception')
    raise ValueError
finally:
    print("Performing cleanup by finally")

'''
'''
try:
    print(54)
    print("abc")
    raise ValueError
except:
    print('123')
finally:
    print("abc123")

'''
#intractive calc model with python operation
#Calculator program
''' using class exception modules '''
class Calculator:
    def __init__(self):
        self.one=0
        self.two=0
    def input_numbers(self):
        try:
            self.one=float(input("Enter 1st number:"))
            self.two=float(input("Enter 2nd number:"))
        except ValueError:
            print("Invalid input....please enter numbers")
            self.input_numbers()
    def add(self):
        return self.one+self.two
    def subtract(self):
        return self.one-self.two
    def multiply(self):
        return self.one*self.two
    def divide(self):
        if self.two==0:
            raise ZeroDivisionError("Cannot divide with zero")
        return self.one/self.two
    def modulo(self):
        return self.one%self.two
    def expo(self):
        return self.one**self.two
    def floor_divide(self):
        return self.one//self.two
def display_menu():
    print("\n === Calculator Menu === \n")
    print("1.Addition(+)")
    print("2.Subtract(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")
    print("5.Modulo(%)")
    print("6.Exponent(**)")
    print("7.Floor_divide(//)")
    print("8.exit")
def main():
    calc=Calculator()
    while True:
        display_menu()
        choice=input("select an operation (1-8):")
        if choice=='8':
            print("Exit")
            break
        calc.input_numbers()
        try:
            if choice=='1':
                print("Result:",calc.add())
            elif choice=='2':
                print("Result:",calc.subtract())
            elif choice=='3':
                print("Result:",calc.multiply())
            elif choice=='4':
                print("Result:",calc.divide())
            elif choice=='5':
                print("Result:",calc.modulo())
            elif choice=='6':
                print("Result:",calc.expo())
            elif choice=='7':
                print("Result:",calc.floor_dvide())
            else:
                print("Invalid choice,select from 1-8")      
        except ZeroDivisibleError as e:
            print("Error:",e)
        except Exception as e:
            print("Unexpected Error:",e)
main()

            
           


















    
