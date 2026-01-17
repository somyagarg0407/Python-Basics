a=int(input("enter your age :"))

#if statement no.1
if(a%2==0):
    print("it is even integer")
#end of if statement no.1 which means that this is independent if statement from below 

#start of if statement no.2
if(a>=18):
    print("your are above the age of consent")

elif(a<=0):
    print("entered age is invalid")

else:
    print("you are below the age of consent")
#end of statement no.2
print("thanks for visiting us")

#use elif multiple time but if only one time when things are co relate to each other