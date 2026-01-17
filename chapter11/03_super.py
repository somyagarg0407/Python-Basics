class employee:
    a=1
    def __init__(self):
        print("constructor of employee")
    

class manager(employee):
     b=2
     def __init__(self):
        print("constructor of maNAGER")
    

class boss(manager):
     c=3
     def __init__(self):
        super().__init__()  #when use it also print constructor of manager which it is linked 
        print("constructor of boss")
    

o=manager
print(o.c)
print(o.b)
print(o.a)

#where the erroris ???


#why we uses self ###########################



