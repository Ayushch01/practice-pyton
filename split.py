var1=input("enter the sentence : ")
list1=[]
temp_word=""
for i in range(len(name1)):
    if var1[i] ==" ":
        list1.append(temp_word)
        temp_word=""
    else:
        temp_word=temp_word+var[i]
list1.append(temp_word)
print("user defined sentence : ",var1)
print("word list : ",list1)

