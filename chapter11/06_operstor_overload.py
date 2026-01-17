class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n+num.n
    


p=number(5)
q=number(10)
print(p+q)


#what is truediv and floordiv in division