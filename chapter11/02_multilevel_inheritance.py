class employee:
    a=1

class manager(employee):
    b=2

class boss(manager):
    c=3

o=employee
print(o.a)
# print(o.b)  #it gives error because employee class not have data of manager class


z=manager
print(z.a,z.b)  #but it gives the output because manager have data of employee also

