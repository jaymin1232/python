#write a program to calculate the bill according to the given slab

print("enter a unit for calculate a rate")
u=int(input("Enter a unit:"))


if u<=100:
    bill=5*u  #u=unit
elif u<=300:
    bill=7*u
elif u<=500:
    bill=9*u
else:
    bill=u*11
print("bill according to given slab:",bill)
    
