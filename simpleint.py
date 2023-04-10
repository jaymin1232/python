#write a program to calculate simple intrest

#for simple intrest we need r=rate,t=time,p=balence SI=p(1+rt)

p=int(input("Enter a balence:"))
r=int(input("Enter a rate of intrest:"))
t=int(input("Enter a time:"))

#process for calculating a simple intrest

SI=int(p*r*t)/100

#output

print("Simple Intrest of your balence is",SI)
