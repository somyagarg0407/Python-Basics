with open("file.txt","r") as f:
    content=f.read()

with open("create new file","w") as f:
    f.write(content)
    
