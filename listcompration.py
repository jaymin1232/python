a = [1,2,3,4,5,6,7,8,9,10]
b = [1,3,5,7,9,11,13,15,17,19]
c = [1,3,5,6,8,16,37,38]
li= 'Z564dsfsd9u9dsu98fsdABFFDHGA'

z=[]
#for i in range(1,21):
    


for i in range(1,21):
    if i%2==1:
        z.append(i)

print(z)

#[filter/expresion traversing(loop) if condition(optional)]

#s=[[i+1,i/2,i**2] for i in a if (i>15)]
#s=[i for i in a for j in b if i==j]
#s=[i for i in a for j in b for k in c if i==j==k]

#a=[i for i in li if i.isalpha()]
#a=[i for i in li if i.isnumeric()]
#a=[i for i in li if i.isupper()]
#a=[i for i in li if i.islower()]

#a=[i.lower() for i in li if i.isupper()]
#a=[i.upper() for i in li if i.islower()]

#str="this is python"
#str2="THIS IS PYTHON"
#print(str.upper())
#print(str2.lower())


#print(a)