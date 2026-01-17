n=int(input("enter number:"))

for i in range(2,n):
    if(n%i==0):
        print("this is not a prime")
        break #important step
else:
    print("number is prime")