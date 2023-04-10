age=int(input("Enter a age:"))

if(age>18 and age<24):
    print("marital start")
    check=int(input("if you are mariied press 1 or not press 2:"))
    if(check==1):
        print("you are disqualified")
    elif(check==2):
        print("you are selected")
    else:
        print("wrong choise")
else:
    print("you are below 18 or abow 24")