# str1=input("enter your string")
# for i in str1:
# 	i=ord(i)
# 	if i>=97:
# 		print(chr(i-32),end="")
# 	else:
# 		print(chr(i+32),end="") 
#SUNNY SIR MAGIC
# x=input("enter your string")
# y=""
# for i in x:
#     if ord(i)>=65 and ord(i)<=90:
#     	a=ord(i)+32
#     	b=chr(a)
#     	y=y+b
#     elif ord(i)>=97 and ord(i)<=122:
#     	y=y+i
#     else:
#     	print("invalid character")
#     	break
# print("value before conversion = ",x)
# print("value after conversion = ",y)
x=input("enter your string")
y=""
for i in x:
    if ord(i)>=65 and ord(i)<=90:
    	a=ord(i)+32
    	b=chr(a)
    	y=y+b
    
    else:
    	y=y+i
print("value before conversion = ",x)
print("value after conversion = ",y)
