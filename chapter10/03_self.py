class employee:
    salary=1200000
    language="python"

    def getInfo(self): #we use def under the class ,and ye self jaisa word likjhan jaruri ahi ye batane ke liye hame kiska get info chahiye
        print(f"the salary is {self.salary},the language is {self.language}")
    
    @staticmethod  #use this if not used self fro general purpose but self is mandotary for ex. above case  
    def greeting():
        print("good night")
    def greet(self): #evenhere self is imp
        print("good morning")    


harry=employee() #remember this
employee.getInfo(harry) 
harry.getInfo()
harry.greet()
harry.greeting()
# we can use either of above two for output
