#immutable data type
#mence after assigning a value you can't change the value

#Numeric



#string

#tuple

'''thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[0])



list=["jaymin","menat","lol","jaymin"]

x = list[0]

print(x)

a = "      Hello, World!         "
print(a.strip())


str1=r'Welcome to \'Python Tutorial\' on MSU'
print(str1)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["a", "b", "c"]
thislist.pop(1)
print(thislist)

print("\n")

print("Membership operator \n")

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list'''


#multiplaction table

'''x=int(input())

for i in range(1,11,1):
    print(x,"*",  i  ,"=",  i*x)'''

#WAP to find inputted number is Armstrong or not
num = int(input("Enter a number: "))

# determine the number of digits in the inputted number
num_digits = len(str(num))

#print(type(num))

# initialize the sum of cubes of digits to 0
sum_of_cubes = 0

# iterate over each digit in the number
for digit in str(num):
   
    # add the cube of the digit to the sum
    sum_of_cubes += int(digit)**num_digits

'''sum of cube = sum of cube + int(digit) ** num_digits 
            = 0     +  0 ** 1 = 3
sum of cube = 3
            = 3     +  1 ** 1 = 9
sum of cube = 9
            = 9     +  2 ** 1 = 12


'''



# check if the sum of cubes is equal to the inputted number
if sum_of_cubes == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


