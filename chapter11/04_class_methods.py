class employee:
    a=1
    @classmethod  #use for showing class attribute even instance attribute is present
    def show(cls):  
        print(f"the class attribute of a is {cls.a}")

e=employee()
e.a=45
e.show()