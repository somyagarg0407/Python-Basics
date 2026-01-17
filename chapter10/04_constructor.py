class employee:
    salary=1200000
    language="python"
     
    def __init__(self,name,salary,language):#dunder(starts and ends with __) method which is automaticall called 
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creat an object") 

harry=employee("harry",14000000,"java")  #this use when we use init method and in the squence of init()

print(harry.name,harry.salary,harry.language)
