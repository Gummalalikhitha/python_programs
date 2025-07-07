'''
IO Oerations/hanling
ASCII textfiles- reading,writing,appen chr
ABC 
656667
b5-binry
66-binary
67-binary
functions for opening and closing file
syntax:
 fileobj=open(filename[,access_model])
access modes -
r   -default mode or opening a file which opens the file for reading only
rb  -opens file in binary formt
r+  -opens both reading/writing
rb+ -opens both reading/writing binary format
w   -opens writing format or creates a file on that name when destination is not provided
wb  -binay format /write
w+  -reading/writing
wb+ -opens both reading/writing binary format
a   -append opens a file to append the data
ab  -appending binary data 
a+  -both reading and appending
ab+ -reading and appending of binary data

file obj attributes 
fileobj.closed -ret -return true if the file is closed and false
otherwise
fileobj.mode   -oprning acess
fileobj.name   -returns the file name

 '''

#I/O Operations
'''
file=open('File.txt',"rb")
print(file.read())                    # b'Hello students!!!!!\r\n'
print(file.read().decode('utf-8') )   # Hello students!!!!!
'''
'''
with open('File.txt',"rb") as f:
    content=f.read().decode('utf-8')   # Hello students!!!!!
    print(content)
'''
'''
with open('File.txt',"w") as f:
    f.write("Wipro,TCS,Capgmini \n")
    f.write("Google,Amazon,HCL \n")
    f.write("Teh Mahindra,L&t,CAT \n")
    print(f)
'''
'''
with open('File.txt',"a") as f:
    f.write("This is a sample appended data")
    print(f)
'''
'''
data=b'This is a sample of binary data'
with open("binary_file.bin","wb") as file:
    file.write(data)
'''
'''
with open('binary_file.bin','r') as file:
    content=file.read()   # This is a sample of binary data- r, #b'This is a sample of binary data' -rb
    print(content)
'''
#filename.seek(pointer_number) ---it modifies 
'''
with open('File.txt','r+') as file:
    content=file.read()
    # file.seek(10)
    file.seek(200)    #if we dont have thatmuch chracters then we will get add 'null' values
    file.write("Modification one here1 \n")
'''
'''
with open('File.txt',"a+") as file:
    file.write('\nAppenedd data')
    file.seek(0)
    print(file.read()) 
'''
'''
with open('File.txt','r') as file:
    lines=file.readlines()
    for line in lines:
        print(line.strip())
print("List of lines:",lines)
'''
#output
# Wipro,TCS,Capgemini
# Google,Amazon,HCL
# Teh Mahindra,L&t,CAT
# This is a sample appended data
# ab cd
# Appenedd data
# List of lines: ['Wipro,TCS,Capgemini \n', 'Google,Amazon,HCL \n', '          Teh Mahindra,L&t,CAT \n', 'This is a sample appended data\n', 'ab cd\n', 'Appenedd data']

'''
with open('file.txt','r') as file:    #Here filename are case-insensitive 
    seperate_lines=[line.strip() for line in file.readlines()]
    print(seperate_lines)
#close() -manually
'''
'''
file=open('File.txt','r')
print(file.closed)   #False
file.close()
print(file.closed)   #True
'''
'''Program to create a txt file acces the textfile data and use the data to split the lines into series of words and use space to perform split opration
split operation
sample.txt
Hello students
How are you today
print:
['Helo','students','how','are','you','today']'''


'''
l=[]
with open("sample.txt",'r+') as f:
    f.write("Hello students ")
    f.write("How are you today")
    f.seek(0)
    content=f.read()
    print(content)
    for i in content.split(" "):
        l.append(i)
print(l)    
'''
# output:
# Hello students How are you today
# ['Hello', 'students', 'How', 'are', 'you', 'today']


with open('File.txt','r') as file1,open('sample.txt','r') as file2:
    content1=file1.read()
    content2=file2.read()
    print("Date of file1:")
    print(content1)
    print("Data of file2:")
    print(content2)
    file1.close()
    file2.close()

