'''
Command line arguements:
sys module
sys.argv-   sys.rgv[0], sys.argv[1]......
error handling
sys.argv ->sys module
index default starts from 0
argparse -flags,optional args
'''

'''
import sys
print("Script name:", sys.argv[0])
print("All args:",sys.argv[1:])
print("Number of items :",len(sys.argv))
print("Including file name :",sys.argv)
if len(sys.argv)>1:
    print("First argv:",sys.argv[1])
else:
    print("No arguments provided")
'''

'''
import sys
num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print("Sum :",num1+num2)
print("Product :",num1*num2*num3)
'''

'''
import sys
if len(sys.argv) !=3:
    print("Usage: python sample.py 1 b")
else:
    l=float(sys.argv[1])
    b=float(sys.argv[2])
    print("Calculated area:",l*b)
'''

'''
import sys
if len(sys.argv)<=1:
    print("Usage:python sample.py n1,n2,...........")
    sys.exit()
numbers=[int(arg) for arg in sys.argv[1:]]
total=sum(numbers)
print("Numbers:",numbers)
print("Sum: ",total)
'''

# Arg using parse
'''
arg names
default values
boolean check
'''
#calc evaluation using parse

import argparse
parser=argparse.ArgumentParser(description="Add 2 numbers")
parser.add_argument('--x',type=int,required=True,help="First number")
parser.add_argument('--y',type=int,required=True,help="Second number")
parser.add_argument('--opt',type=str,required=True,choices=['add','sub','mul','div'],help="Operation")
args=parser.parse_args()
if args.opt=='add':
    result=args.x+args.y
elif args.opt=='sub':
    result=args.x-args.y
elif args.opt=='mul':
    result=args.x*args.y
elif args.opt=='div':
    result=args.x/args.y
print("Result is ",result)












