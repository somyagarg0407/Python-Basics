p1="buy this"
p2="check this"

message=input("enter your comment:")

if((p1 in message) or (p2 in message)):
    print("this is spam")

else:
    print("this is not a spam")    