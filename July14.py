# ''' Reverse of a array '''

# n=list(map(int,input().split(" ")))
# l,r=0,len(n)-1
# while(l<=r):
#     n[l],n[r]=n[r],n[l]
#     l+=1
#     r-=1
# print(n)

# l=list(map(int,input().split(" ")))
# print(l[::-1])
# l.reverse()
# print(l)

# n=list(map(int,input().split(" ")))
# s,l=[],[]
# for i in range(3):
#     s.append(min(n))
#     n.remove(min(n))
#     l.append(max(n))
#     n.remove(max(n))
# print("Minimum 3 elements are :",s)
# print("Maximum 3 elements are :",l)

# import random
# from collections import Counter
# l=[random.randint(1,101) for i in range(1,31)]
# # print(l)
# a=dict(Counter(l))
# # print(a)
# for i in range(1,100):
#     if i in a:
#         print(f"Mark with {i} are {a[i]} students go it")
#     else:
#         print(f"Mark with {i} are 0 students go it")



# import random
# l=[random.randint(1,101) for i in range(1,11)]
# print(l)
# intervals={"a10":0,"a20":0,"a30":0,"a40":0,"a50":0,"a60":0,"a70":0,"a80":0,"a90":0,"a100":0}
# for i in l:
#     if 0<=i<=10:
#         intervals['a10']+=1
#     elif 11<=i<=20:
#         intervals['a20']+=1
#     elif 21<=i<=30:
#         intervals['a30']+=1
#     elif 31<=i<=40:
#         intervals['a40']+=1
#     elif 41<=i<=50:
#         intervals['a50']+=1
#     elif 51<=i<=60:
#         intervals['a60']+=1
#     elif 61<=i<=70:
#         intervals['a70']+=1
#     elif 71<=i<=80:
#         intervals['a80']+=1
#     elif 81<=i<=90:
#         intervals['a90']+=1
#     elif 91<=i<=100:
#         intervals['a100']+=1
# for i in intervals:
#     print(f"No of students in {i} are : {intervals[i]}")


''' String Operations '''

# a=input()
# print(len(a))
# print(a+".")
# print(a[::-1])
# c=0
# for i in a:
#     if i in "aeiou":
#         c+=1
# print(c)

# s=input()
# rev_s=""
# for i in s:
#     rev_s=i+rev_s
# print(rev_s)

# s=input()
# ovel_s=""
# for i in s:
#     if i in "aeiou":
#         ovel_s=ovel_s+"z"
#     else:
#         ovel_s=ovel_s+i
# if ovel_s==s:
#     print("No vowel found")
# else:
#     print(ovel_s)

# str1=input()
# str2=input()
# print(str1+str2)
# s=""
# for i in str2:
#     s=i+s
# print(str1+s)

# s=input()
# for i in set(s):
#     print(f"The letter {i} has repeated for {s.count(i)} times in string {s}")


''' Sort and Searching techniques '''
''' Ascening order after merge'''
# arr1=list(map(int,input().split(" ")))
# arr2=list(map(int,input().split(" ")))
# # arr1.extend(arr2)    #arr1=arr1+arr2
# for i in range(len(arr1)):
#     for j in range(i+1):
#         if arr1[i]<=arr1[j]:
#             arr1[i],arr1[j]=arr1[j],arr1[i]
# print(arr1)

'''Descending order'''
# l=list(map(int,input().split(" ")))
# for i in range(len(l)):
#     for j in range(i+1):
#         if l[i]>=l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

