dict1={"name":"deepak","class":"BCA","subject":"commerce"}
dict2={1:"23",2:"25",3:"26",3:"27"}
for i,j in dict1.items():
	print(i)
	print(j)
for i,j in dict2.items():
	print(i)
	print(j)
dict1["name"]="sunny"
print(dict1)
dict1["school"]="nahi pata"
print(dict1)
dict1.pop("subject")
print(dict1)