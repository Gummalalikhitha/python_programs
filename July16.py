# n=[i**2 for i in range(1,int(input())+1)]
# print(n)

# import random
# a=[i**2 for i in range(1,random.randint(1,11))]
# print(a)

# code to tAKE USER INPUT Of RANDOM 10 NUMBERSUING LIST COMPREHENSION AND print them if more than 10 numbers are given then ignore the remaining elements
# print([i for i in list(map(int,input().split(" ")))[:10]])

#print([i for i in list(map(int,input().split(" ")))[:10] if i%2==0])

# color=['red','blue','yellow','violet','black','white']
# print([i.upper() for i in color])

# m=[[1,2,3],[4,5,[6,[3,4]]],[7,8,9]]
# print(m[1][2][1][1])

'''code to take uer input with space seperated and convert th 9 input in to 3X3 matrix form on display'''



# n=list(map(int,input().split(" ")))[:9]
# l=[[i for i in n[i:i+3]] for i in range(0,len(n),3)]
# for i in l:
#     print(i)


# n=[int(x) for x in input("Enter 9 nums: ").split()[:9]]
# m=[[n[i*3+j] for j in range(3)] for i in range(3)]
# print("3X3 Matrix")
# for x in m:
#     print(x)


'''code to convert dec to binay matrix by considering even and odd manipulations for user defined variables of an nXn matrix where n=3
list=[[1,2,3],[3,3,3],[4,5,6]] '''

# n=[[1,2,3],[3,3,3],[4,5,6]]
# l=[1 if i%2!=0 else 0 for j in n for i in j]
# print(l)
# for i in range(0,len(l),3):
#     print(*l[i:i+3])

# print()
# n=[[1,2,3],[3,3,3],[4,5,6]]
# l=[[1 if i%2!=0 else 0 for i in j] for j in n]
# for i in l:
#     print(*i)



# * * * * * * *
# * * * _ * * *
# * * _ _ _ * *
# * _ _ _ _ _ *
# * * _ _ _ * *
# * * * _ * * *
# * * * * * * *

# n=9
# p=[" ".join("_" if (abs(i-n//2)+abs(j-n//2)<n//2) and i!=0 and i!=n-1 else "+"for j in range(n)) for i in range(n)]
# for r in p:
#     print(r)













    