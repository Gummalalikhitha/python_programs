# import re
# n=input()
# a=re.findall(r'[0-7]{3}',n)
# print(a)

# import re
# a=input()
# b=re.findall(r"(\w+)@([a-zA-Z]+).(a-zA-Z{2,})",a)
# print(b)
# for i,j,k in b:
#     print(i,j,k)

# import re
# a=input()
# b=re.match(r'(\w+)@([a-zA-Z]+)\.([a-zA-Z]{2,})',a)
# if b:
#     print(b.group(1))
#     print(b.group(2))
#     print(b.group(3))
# else:
#     print("Invalid")

# import re
# a=input()
# b=re.findall(r'[a-zA-Z]+',a)
# print(b)
# if b:
#     for i in b:
#         print(i,end=" ")


# import re
# str=input()
# a=re.match(r'\w+',str)
# if a:
#     b=a.group()
#     print(b[0]==b[-1])
