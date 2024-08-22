#data tyes: 1-fundamentals 2-compound(list,tupple,dictionary)
#There are five fundatmentals data types-int,float,bool,str,complex
x=123
y='123a'
z=123.45
n=True
print(type(x)) #int
print(type(y)) #str
print(type(z)) #float
print(type(x>z)) #bool
print(type(n)) #bool

#when we perform any mathmatical operationn on boolean value , its is going to be matmatical(True -1, False -0)
print(True+True) #result will be 2

#int,float and boolean is known as number data types-we can perform mathmatical operation among them
print(x+True)

#any value written in the quotation mark will be considered as string
m="123.45"
print(type(m))

#-------------------------------------**---------------------------------------------------------------
#Quotaion Mark in python
#'',"",''''''  three types of quotation mark
#''-> while writing any character or word
#""->while writing any line(multiple word)
#''''''->multi line string

print('ashish')
print("ashish kumar's singh")
c='''hello
ashish
kumar
singh'''
print(c)