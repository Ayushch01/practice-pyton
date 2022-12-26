# x=int(input("enter the value:"))
# fact=1
# if x==0 and x==1:
# 	fact=1
# else:
# 	for i in range(1,x+1):
# 		fact=fact*i
# print(fact)
def func(x):
	fact=1
	if x==0 and x==1:
		fact=1
	else:
		for i in range(1,x+1):
			fact=fact*i
	return fact
for i in range(2):
	choice=int(input("enter your values : "))
	fact1=func(choice)
	print(fact1)