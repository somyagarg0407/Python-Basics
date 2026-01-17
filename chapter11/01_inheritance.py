class employee:
    def show(self):
        print(f"the name is {self.name} ")

class programmer(employee): #here we use employee as base class for programmer class it means all def of base class are added in derived (programmer) class
    def salary(self):
        print(f"the salary is {self.salary}")

#for multiple inheritance can also use anither cclass in bracket by comma like class programmer(coder.employee)
