# typing a find a factorial of number

'''5! = 5*4*3*2*1 = 120''' 

'''number = int(input("Enter a number for finding a factorial:"))

count=1

for i in range(1,number + 1):
    count=count*i
      
print("factorial of given number is:",count)


#givien number is armstrong or not'''

''' 6   = 6 to the power of (number of digit) 1 = 6 ==> armstrong number 
    12  = 12 to the power of (number of digit) 2 = 1 to power 2 +  2 to the power 2 = 5 ==> not an armstrong number  
    134 =
    '''
number = int(input("Enter a number for finding that number is Armstrong or not:"))

len_of_digit = len(str(number))  #stroning a number lenth

sum_of_cube = 0 
for digit in str(number):

    sum_of_cube = sum_of_cube + int(digit) ** len_of_digit

if(sum_of_cube == number):
    print("Number is an Armstrong")
else:
    print("Nmber is not an Armstrong")

    






