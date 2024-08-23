age=40
if age:
    print("print line")
else:
    print("don't print")

#-------------------------------**-----------------------------------------------------

x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
if x!=y:
    if x>y:
        print("x is greater than y")
    else:
        print("y is greater than x")
else:
    print("both are equal")

#-----------------------------------------**------------------------------------------
#in case we have more than one condition, then we use elif.
#(con1 and con2) or con3
day=input("Enter day:")
amount=int(input("enter the amount:"))
if day.lower()=='sunday' and amount>5000:
    dis=(amount*10)/100
    amount=amount-dis
    print("after 10% discount price will be :",amount)
elif day.lower()=='sunday' and amount>4000:
    dis=(amount*5)/100
    amount=amount-dis
    print("after 5% discount price will be :",amount)
else:
    print("without discount price will be :",amount)
