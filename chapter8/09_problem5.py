def rem(l,word):
    n=[]
    for item in l:
        if not (item==word):
            n.append(item.strip(word))
        return n

l=["sohan","somya","an"]
print(rem(l,"an"))   

#i dont understand this even not know why use strip