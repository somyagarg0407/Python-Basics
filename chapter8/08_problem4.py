def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)  

pattern(10)
print(pattern(10))  #ye end main pattern (10) ki return value dega which is none


#if you already using word "print" above in function so dont use during input