def generatetable(n):
    table=""  #why use this
    for i in range(1,11):  #why not use n instead of i
        table+=f"{n}X{i}={n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:  #ye tables/table_ kyun kiya
        f.write(table)

for i in range(2,21):
    generatetable(i)
