class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)


    def __str__(self):  #use kiya jisse ham commplex ka asn jan paaye
        return f"{self.r} + {self.i}"
    

c1=complex(5,4)
c2=complex(6,5)

print(c1+c2)

#why syntax error
