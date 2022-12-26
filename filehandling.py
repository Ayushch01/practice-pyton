# var1=open("intro.txt","a")
# var1.write("ayush chaturvedi")
# var1.close()
# var1=open("intro.txt","r")
# data=var1.read()
# print(data)
# var1.close()
'''f=open("telephone.txt","a")
name=input("enter your name : ")
age=input("enter your age : ")
city=input("enter your city : ")
detail="Hi I am {} .\n I am {} years old.\n I live in {}.".format(name,age,city)
print(detail)
f.write(detail)
f.close()'''
#nextone
# f=open("telephone.txt","r")
# data=f.read()
# print(data)
# f.close()


#step1


marks=open("marks.txt","w")
student_name=input("enter student name: ")
english_marks=input("enter your eng marks : ")
hindi_marks=input("enter your hindi marks : ")
maths_marks=input("enter your maths marks : ")
detail=" {},{},{},{}".format(student_name,english_marks,hindi_marks,maths_marks)
marks.write(detail)
marks.close()

#step2 : reading marks from marks.txt and calculating total and average

record=open("marks.txt","r")
data=record.read()
print(data)

record.close()

# var1=open("hw.txt","a")
# add=english+hindi+maths
# detail="Total= {}.".format(add)
# print(detail)
# var1.write(detail)
# avg=("english"+"hindi"+"maths")/3
# detail="Average= {}.".format(avg)
# print(detail)
# var1.write(detail)
# var1.close()

