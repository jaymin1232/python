# wrp menu drive program to find area of triangle, circle, rectangle, square and cylinder.

print("Select area that you want to find")
print("For triangle press 1\n For circle press 2\n For rectangle press 3\n For square press 4\n For cylinder press 5")
x=int(input(":-"))

if(x==1):
        print("for triangle")
        b=int(input("Enter a base:"))
        h=int(input("Enter a height:"))
        area=0.5*b*h
        print(area)
        
elif(x==2):
        print("for circle")
        r=int(input("Enter a radiuse:"))
        area=3.14*r*r
        print(area)
        
elif(x==3):
        print("for rectangle")
        l=int(input("Enter a lenth:"))
        w=int(input("Enter a width:"))
        area=l*w
        print(area)
elif(x==4):
       print("for square")
       l=int(input("enter a lenth:"))
       area=l*l
       print(area)
else:
    print("wrong choise try again....")



