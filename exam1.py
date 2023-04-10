#WRP to print the second largest odd number in the given list 
N=[8,9,12,61,89,78,86,21,"Shanu","Rahul"]

number=[]
odd_number=[]
value_sort=[]
#separate a number in list
for i in range(0,8):{        
    number.append(N[i])
    #print(N[i]
}
#in separate number findding a odd number
for i in number:
    if(i%2 == 1):
        odd_number.append(i)
#sort in assending order and store in another variable
print(odd_number.sort())
for i in range(0,4):
    value_sort.append(odd_number[i])
    #print(odd_number[i])
#print(odd_number[-2:-1:])
#print(odd_number)
#printing a secondlast number in list using slicing
second_largest = odd_number[-2]
print(second_largest)




