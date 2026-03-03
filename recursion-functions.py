#calculate factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
    

print(factorial(1))

#sum of first n number using recursion
def sum(m):
    if (m==0):
        return 0
    return  sum(m-1) + m

print(sum(5))