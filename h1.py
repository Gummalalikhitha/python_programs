#Searching Techniques
'''
def linear_search(arr,tar):
    k=0
    while k<len(arr):
        if arr[k]==tar:
            return k
        k+=1
    return -1
arr=list(map(int,input().split(" ")))
tar=int(input())
print(linear_search(arr,tar))
'''
'''
def binary_search(arr,tar):
    l,h=0,len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            l=mid+1
        elif arr[mid]>tar:
            h=mid-1
    return -1
arr=list(map(int,input().split(" ")))
tar=int(input())
print(binary_search(arr,tar))



def binary_search(arr,tar):
    l,h=0,len(arr)-1
    a=arr[:]
    arr.sort()
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==tar:
            return a.index(arr[mid])
        elif arr[mid]<tar:
            l=mid+1
        elif arr[mid]>tar:
            h=mid-1
    return -1
arr=list(map(int,input().split(" ")))
tar=int(input())
print(binary_search(arr,tar))
'''
#Sorting Techniques
'''
def bubble_sort(arr):
    flag=True
    while flag:
        flag=False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                flag=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
    return arr
arr=list(map(int,input().split(" ")))
print(bubble_sort([3, 9, 2, 8, 4, 7, 6, 1, 5, 0]))
'''
'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr
arr=list(map(int,input().split(' ')))
print(insertion_sort(arr))
'''
'''
def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=list(map(int,input().split(" ")))
print(selection_sort(arr))
'''
'''
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    L=merge_sort(arr[:mid])
    R=merge_sort(arr[mid:])
    l,r=0,0
    sorted_arr=[0]*len(arr)
    i=0
    while l<len(L) and r<len(R):
        if L[l]<R[r]:
            sorted_arr[i]=L[l]
            l+=1
        else:
            sorted_arr[i]=R[r]
            r+=1
        i+=1
    while l<len(L):
        sorted_arr[i]=L[l]
        l+=1
        i+=1
    while r<len(R):
        sorted_arr[i]=R[r]
        r+=1
        i+=1
    return sorted_arr
arr=list(map(int,input().split(" ")))
print(merge_sort(arr))

class Solution(object):
    def twoSum(self, numbers, target):
        i,j=0,1
        while(i<len(numbers) and j<len(numbers)):
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif (numbers[i]+numbers[j]<target):
                if j!=len(numbers)-1:
                    j+=1
                else: 
                    i+=1
                    j=i+1
            else:
                i+=1
                j=i+1
        return []
            
                
            

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

def canJump(nums):
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            print("i,nums[i],i+nums[i],goal",i,nums[i],i+nums[i],goal)
            if i+nums[i]>=goal:
                goal=i
                print(goal)
        return goal==0      
nums=list(map(int,input().split(" ")))
print(canJump(nums))

def productExceptSelf(nums):
        res = []
        
        acc = 1
        for n in nums:
            res.append(acc)
            acc *= n
            print(res,acc,n)

        acc = 1
        print(res)
        for i in reversed(range(len(nums))):
            res[i] *= acc
            print(res[i],acc,nums[i],'----')
            acc *= nums[i]
            print(res[i],acc,nums[i])
            
        return res
nums=[1,2,3,4]
print(productExceptSelf(nums))


def isValid(s):
        a={'(':')','{':'}','[':']',')':'(','}':'{',']':'['}
        l=[]
        for i in s:
            if i in l:
                    l.pop()
            else:
                    if  i in "}])":
                            continue
                    else:
                            l.append(a[i])
        return len(l)==0 
s="(){}}{"
print(isValid(s))

def closestPrimes(left, right):
        l=[]
        temp,a,b=float('inf'),0,0
        for i in range(left,right+1):
            a=all(i%j!=0 for j in range(2,i))
            if a:
                l.append(i)
        #print(l)
        if len(l)<2:
            return [-1,-1]
        else:
            for i in range(1,len(l)):
                if l[i]-l[i-1]<temp:
                        #print(l[i],l[i-1],temp)
                        temp=l[i]-l[i-1]
                       # print(l[i],l[i-1],temp,l[i]-l[i-1]<temp)
                       # print(l[i],l[i-1],temp)
                        a,b=l[i-1],l[i]
            return [a,b]
print(closestPrimes(10,19))

def isSubsequence(s, t):
        a=list(s)
        for i in t:
                if i in a and i==a[0]:
                        print(a,i)
                        a.pop(0)
                        print(a,i)
                print(i)
        print(a)
        return len(a)==0
print(isSubsequence('abc','ahbgdc'))

def wordPattern(pattern, s):
        d={}
        e={}
        l=s.split(" ")
        k=[]
        for i in range(len(pattern)):
            if pattern[i] in d:
                k.append(d[pattern[i]]==l[i])
            else:
                d[pattern[i]]=l[i]
            if l[i] in e:
                k.append(e[l[i]]==pattern[i])
            else:
                e[l[i]]=pattern[i]
        return all(i for i in k)
print(wordPattern('abba','dog dog dog dog'))

def isprime(a,b):
        l=[]
        if 
        for i in range(a,b+1):
                for j in range(2,int(i**0.5)+1):
                                if i%j==0:
                                        return False
                        l.append(j)
                        print(l)
        return l
a,b=map(int,input().split())
print(isprime(a,b))
                     
def print_primes_between(a, b):
    temp=float('inf')
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    if a > b:
        a, b = b, a  # Swap to ensure correct range
    primes = [num for num in range(a , b+1) if is_prime(num)]
    print(primes)
    if len(primes)<=1:
            return [-1,-1]
    else:
            for i in range(1,len(primes)):
                    if primes[i]-primes[i-1]<temp:
                            temp=primes[i]-primes[i-1]
                            a,b=primes[i-1],primes[i]
            return [a,b]
# Example usage:
print(print_primes_between(255322,929209))
'''
#Reverse of string
'''
def hanief(x):
    print(str(x)[::-1])
x=eval(input())
hanief(x)
 '''
#divisible by 5 and greater than 150
'''
n=eval(input())
l=[]
for i in n:
    if i%5==0 and i<=150:
        l.append(i)
    if i%5==0 and i>150:
        break
print(l)
'''
#multiplication of two numbers
'''
def multiplication(num1,num2):
    if num1*num2>1000:
        return num1+num2
    return num1*num2
num1=int(input())
num2=int(input())
print(multiplication(num1,num2))
'''
#sum of numbers in a range
'''
n=int(input())
s=0
for i in range(n+1):
    s=s+i
print(s)
'''
#sum of numbers of squares
'''
n=int(input())
s=0
for i in range(n+1):
    s=s+i**2
print(s)
'''
#sum of numbers of cubes
'''
n=int(input())
s=0
for i in range(n+1):
    s=s+i**3
print(s)
'''
#n+nn+nnn
'''
n=int(input())
#print(int(n),int(str(n)*2),int(str(n)*3))
print(int(n)+int(str(n)*2)+int(str(n)*3))
'''
#count of the digits
'''
n=int(input())
print(len(str(n)))
'''
#generate a range
'''
a=int(input())
l=[i for i in range(a+1)]
m=[j for j in range(a+1)]
m.insert(0,0)
m.pop()
for i in range(a+1):
    print(l[i],m[i],l[i]+m[i])
'''
#natural numbers
'''
n=int(input())
i=1
while(i<=n):
    print(i,end=" ")
    i=i+1

#even characters
n="programming"
for i in range(len(n)):
    if i%2==0:
        print(i,n[i])


#printing right angled triangle
n=5
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    for l in range(1,i):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n,i,-1):
        print("*",end="")
    for l in range(n-1,i,-1):
        print("*",end="")
    print()

n=input()
a=tuple(n)
l=[]
for i in a[::-1]:
    if i!="(" or i!=")" or i!=",":
        l.append(l)
print(l)


n=int(input())
if n%2==0: print("Even")
else: print("Odd")
'''
#Matrix Transponse
'''
r=int(input())
c=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
for i in l:
    print(i)
for i in range(r):
    for j in range(i):
        l[i][j],l[j][i]=l[j][i],l[i][j]
print()
for i in l:
    print(i)
'''

'''  
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
m=int(input())
l=[]
a=""
for i in range(n):
    for j in range(m):
        t=list(map(str,input().split(" ")))
        l.append(t)
print(l)
#         if b!="wall":
#             a=a+"-->"
#         a=a+"\next"
# print(str(a[:-1]))
'''
'''
l=[]
nums=[0,0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
for i in range(1,len(nums)):
    if nums[i]==nums[i-1] and nums[i-1] not in l:
        l.append(nums[i-1])
    elif nums[i]!=nums[i-1] and nums[i] not in l and nums[i-1] not in l:
        l.append(nums[i])
        l.append(nums[i-1])
nums=l
print(nums)
'''
'''
nums=[1,1,0,1]
temp,i,c,s,d=0,1,1,True,{}
for i in range(1,len(nums)):
    if nums[i-1]==nums[i]:
        c+=1
        d[temp]=c
    else:
        d[temp]=c
        c=1
        temp=i
print(d)
v=d.values()
k=d.keys()
print(list(v).index(max(list(v))))
print(list(k)[list(v).index(max(list(v)))])
'''

#Recursion

#printing numbers from n to 1
'''
def print_reverse(n):
    if n==0:
        return 
    print(n,end=" ")
    return print_reverse(n-1)
print_reverse(6)
print()
print_reverse(20)
'''

#sum of first n numbers
'''
def sumn(n):
    if n==0:
        return 0
    return n+sumn(n-1)
print(sumn(2))
'''
#sum of all numbers in array
'''
def sumarray(arr,n):
    if n==0:
        return 0
    return arr[n-1]+sumarray(arr,n-1)
print(sumarray([1,2,3,4,5],5))
'''
#factorial of n
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
'''
#power of two
'''
def ispoweroftwo(n):
    if n==1:
        return True
    if n<0 or n%2!=0:
        return False
    return ispoweroftwo(n//2)
print(ispoweroftwo(641))
'''
#Searching and Sorting
#Linear Search
'''
t=9
a=[8,3,6,1,9,7,4,2,10]
for i in range(len(a)):
    if a[i]==t:
        print(i)
        break
else:
    print(-1)
'''
#Binary Search
'''
t=2
a=[0, 1, 2, 3, 4, 5, 6, 7, 10, 13]
l,h=0,len(a)-1
while(l<=h):
    m=(l+h)//2
    if a[m]==t:
        print(m)
        break
    elif a[m]<t:
        l=m+1
    else:
        h=m-1
else:
    print(-1)
'''
#Bubble Sort
'''
a=[5,0,9,2,8,4,7,6,1,3]
flag=True
while flag:
    flag=False
    for i in range(1,len(a)):
        if a[i-1]>a[i]:
            flag=True
            a[i],a[i-1]=a[i-1],a[i]
print(a)
'''
#Selection Sort
'''
a=[15,16,6,8,5]
for i in range(len(a)):
    t=i
    for j in range(i+1,len(a)):
        if a[t]>a[j]:
            t=j
    a[i],a[t]=a[t],a[i]
print(a)
'''
#Insertion Sort
'''
a=[9, 2, 8, 4, 7, 6, 1, 3, 5, 0]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
'''
def merge_sort(a):
    if len(a)==1:
        return a
    mid=len(a)//2
    L=merge_sort(a[:mid])
    R=merge_sort(a[mid:])
    l,r,i=0,0,0
    sort_a=[0]*len(a)
    while(l<len(L) and r<len(R)):
        if L[l]<R[r]:
            sort_a[i]=L[l]
            l+=1
        else:
            sort_a[i]=R[r]
            r+=1
        i+=1
    while l<len(L):
        sort_a[i]=L[l]
        i+=1
        l+=1
    while r<len(R):
        sort_a[i]=R[r]
        i+=1
        r+=1
    return sort_a
a=[16,8,20,0,5,9,15,1,6]
print(merge_sort(a))
        
            
    

