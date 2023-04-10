#wrp to print a prime number

x=int(input("Enter a number:"))

c=0

for i in range(1,x+1):                                 
    if x%i==0:
        c=c+1
if c==2:
    print("number is prime number")
else:
    print("number is not a prime number")

'''
x=4
range(1,5) // i= 1,2,3,4
if 4%1==0 (true)
        c =0+1 => 1
   4%2==0 (true)
        c =1+1 => 2
   4%3==0 (false)
        (can't execute)
    4%4==0 (true)
        c =2+1 => 3
c==2 is not a prime number

x=53
range(1,15) // i=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
if 53%1==0 (t)
  
53%2==0 (f) 
    (can't execute)
53%3==0 (f) 
    (can't execute)
53%4==0 (f) 
    (can't execute)
53%5==0 (f) 
    (can't execute)
53%6==0 (f)
    (can't execute)
53%7==0 (f) 
    (can't execute)
53%53==0 (t)
'''