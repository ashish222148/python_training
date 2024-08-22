#function
# help(print)
# help(input)

print('Hello')
print('Ashish')

print('Hello',end=' ')
print('Ashish')

row1=[101,'amit',23,'delhi']
for x in row1:
    print(x,end=',')
    print()

#---------------------------------------------**----------------------------------------------------
#input function always return a string value
x=input("enter the first number:")
y=input("enter the second number:")
print(type(x))
z=x+y
print(z)

#------------------------------**----------------------------------------------------------------
#type casting
#specific to txt file not for csv
#when we read data of txt file , it will be in string, then we need to do type casting
m=open(r'C:\Users\Admin\Desktop\abc.txt').read()
print(type(m),m)

#when we excute any bash command through python, we get the out put in form of string, type casting required