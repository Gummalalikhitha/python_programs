'''Numpy Module'''
# numpy
# matrices -coordinates location
# math function statistics /algebra
'''
np.random.rand()  ---uniform random values 
np.random.randn() ---non uniform 
np.dot            ---multiplication of matrices
np.arange()       ---random range of values
np.array()        ---create /delete /access
np.zeros()/ones() ---create an rentire array with 0/1
np.mean()        
np.std()
np.unique()
np.linalg.inv()
'''

# Arrays-import numpy
'''
import numpy as np
x=np.array([1,2,3,4,5])
print("Array 1-D",x)

y=np.array([[1,2],[3,4]])
print("Array 2-D\n",y)

o=np.ones((3,6))   #It give us theall elements as 1
print('ones  \n',o)

o=np.ones((3,6),dtype=int)
print('ones with integer type \n',o)

o=np.zeros((3,6),dtype=int)
print("zeros with integer type \n",o)

o=np.zeros((3,6))  #it give us matrix of all elements AS 0 
print("zeros \n",o)

o=np.eye(3)
print("Identical coordinates \n",o)

o=np.eye(3,dtype=int)  #it give us identity matrix 
print("Identical coordinates \n",o)

a=np.arange(0,11,2)
print("Array:",a)

b=np.linspace(0,1,5) #it will slice exactly with equally space in between the elements
print("linspace: ",b)
'''
'''operations on arrays using numpy'''

import numpy as np
# a1=np.array([1,2,3,4])
# a2=np.array([5,6,7,8])
# print(a1,a2)
# print("Addition: ",a1+a2)
# print("Product: ",a1*a2)
# print("Square: ",a1**2)
# print("sin values:",np.sin(a1))
# print("Mean :",np.mean(a1))
# print("Max :",np.max(a1))
# print("Min :",np.min(a1))

a=np.arange(1,10)  #<class 'numpy.ndarray'>
print(a)
reshaped=a.reshape((3,3))
print(reshaped)

b=[1,2,3,4]  #<class 'list'>
print(np.array(b).reshape((2,2)))

a=np.arange(1,10)
reshaped=a.reshape((3,3))
print(reshaped)
print("element at (1,1):",reshaped)
linear=reshaped.reshape(-1)  #li=reshaped.flatten()  #both has same function
print(linear)
li=reshaped.flatten()
print("greater than 5:",linear[linear>5])
print("less than 5 :",li[li<5])
print("Random numbers between 0 to 3:",np.random.rand(3))
print("random integer:\n",np.random.randint(100,size=(2,3)))


'''ADES-Advance Data Structure'''
'''linked list perform the insert at begining and deleting at end ,double/circular linkedlist'''
'''find duplicate element in linkedlist and find its occurance'''
'''trees,graphs'''

'''code to print a 3x3 matrix which were filled with boolean value True using numpy'''
import numpy as np
a=np.ones(9,dtype=bool)
# print(a)
b=a.reshape((3,3))
print(b)

import numpy as np
arr=np.full((3,3),True)
print(arr)
