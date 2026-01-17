def f_to_c(f):
    return 5*(f-32)/9

f=int(int(input("enter number :")))

c=f_to_c(f)
print(f"{round(c,2)}degree celcius")

#use round for rounding off to two digit for rounding 2 digit we write 2 after apply comma to that variable
