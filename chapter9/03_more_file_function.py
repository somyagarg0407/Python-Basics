f=open("file.txt")
# data=f.readlines()
# # line1=f.readline()  #can also use this for single line reading
# print(data,line1,type(data))
# f.close()
#this helps to read line by line(pehle 1st line then 2nd line then.....)

#when i try to print line no. 5 it give my empty string("") because line 5 does ot exist

#or you can use for save time

line=f.readline()
while(line!=""):   #!= means does not equal to
    print(line)
    line=f.readline() #why i write this extra line 

f.close()