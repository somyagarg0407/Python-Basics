class employee:
   
    a=1
    @classmethod  #use for showing class attribute even instance attribute is present
    def show(cls):  
        print(f"the class attribute of a is {cls.a}")
    

    @property
    def name(self):
        return f"{self.fname},{self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]  #why value is use here
        self.lname=value.split(" ")[1]       
        



e=employee()
e.name="somya garg"

print(e.fname)
print(e.lname)
e.show()
