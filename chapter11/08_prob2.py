class employee:
    salary=100
    increment=20  #in percentage
    
    @property
    def salaryafterincrement(self):
        return (self.salary*(1+(self.increment/100)))  #difference between return and
    
    @salaryafterincrement.setter   #ye use kiya jisse ham input main salary after increment dekar increment jaan sake
    def salaryafterincrement(self,salary):
        self.increment=(((salary/self.salary)-1)*100)

a=employee()
# print(a.salaryafterincrement)


a.salaryafterincrement=140
print(a.increment)

#why it show 39.999999 not 40




