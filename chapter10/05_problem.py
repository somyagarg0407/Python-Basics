class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"{self.n*self.n}")

    def squareroot(self):
        print(f"{self.n**1/2}")   #whats the problem


a=calculator(16)
a.square()
a.squareroot()