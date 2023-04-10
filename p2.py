
print("What you want to perform")

print("for add enter 1:")
print("for sub enter 2:")
print("for mul enter 3:")
print("for div enter 4:")

c=int(input("Enter a choise:"))

a=int(input("enter a number for a:"))
b=int(input("enter a number for b:"))

if c==1:
    add=a+b
    print("Addtion of a and b is:",add)
elif c==2:
    sub=a-b
    print("substraction of a and b is:",sub)
elif c==3:
    mul=a*b
    print("multipliction of a and b is:",mul)
elif c==4:
    div=a/b
    print("division of a and b is:",div)
else:
    print("wrong choice")
    


