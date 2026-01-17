def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("enter number:"))
print(f"factorial of n is: {factorial(n)}") 

#use recursion when yoy know about formula or identity about it

