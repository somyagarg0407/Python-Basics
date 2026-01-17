f=open("file.txt")  
data=f.read()
print(data)
f.close

#you can also use

with open("file.txt") as f:
    print(f.read())

#by this you dont need to explicitily(??) close the file