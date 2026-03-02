#enter the number and calculate the table of the that number
x=int(input("enter the number you want to see the table of :"))
num=1
while(num<=10):
    print(x*num)
    num=num+1




#print the elements of the list
lista=[1,2,3,4,5,6,7,454,22,11,12]
ind=0
while ind<len(lista):
    print(lista[ind])
    ind=ind+1



#search a number in the tuple using while loop 
tupp=(1,2,3,4,5,6,7)
i=0
while i<len(tupp):
    if(tupp[i]==3):
        print("found at index",i)
    i=i+1



#search for a number using for loop
number=[1,2,4,5,6,7,8,45,33,22]
x=2
for n in number:
    if(n==x):
        print("number found at index",x)




#multipication table using for loop
nn=int(input("enter the number you want to see the table of: "))
for table in range(1,11,1):
    table=table*nn
    print(table)




#factorial of n numbers
inputt=int(input("enter the number you want the factorial: "))
factorial=1
for fact in range(1,inputt+1):
    factorial=factorial*fact
print(factorial)


    
