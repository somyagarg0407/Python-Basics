marks={
       "sohan":54,
       "rohan":52,
       "somya":100,
       "virat":99,
       "kohli":[1,2,3]
}

print(marks.items()) #in ordered pair
print(marks.keys()) #L.H.S.
print(marks.values())#R.H.S.

marks.update({"somya":99,"cherry":50}) 
print(marks)

print(marks.get("somya"))

print(marks.get("somya2")) #it prints none
print(marks["somya2"]) #it return an error

#explore more from chat gpt


b={} # empty dict