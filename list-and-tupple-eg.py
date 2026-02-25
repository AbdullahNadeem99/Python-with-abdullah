#take input of three movies and stores them in the list.
listt=[]
movie1=input("enter the name of your most fav movie ")
movie2=input("enter the name of the second fav movie")
movie3=input("enter the name of the third fav movie")
listt.append(movie1)
listt.append(movie2)
listt.append(movie3)
print(listt)

#check if a list is paliindrome
list2=[1,2,3,2,10]
copy_list=list2.copy()
copy_list.reverse()
if(list2==copy_list):
    print("palindrome")
else:
    print("not palindrome")
   
#count num of a in a tupple

tup=("A","B","C","A","B","A")
count=tup.count("A")
print(count)

#convert that tup to list and sort
my_list=list(tup)
print(my_list)
my_list.sort()
print(my_list)