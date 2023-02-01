#1st
# class student:
#     def __init__(self,name,course,subject):
#         self.name=name
#         self.course=course
#         self.subject=subject
#     def show(self):
#         print("Name :",self.name)
#         print("Course :",self.course)
#         print("Subject:",self.subject)
# s1=student("Ram","BCA","Python")
# s1.show()

#2nd

class student:
    def __init__(self):
        self.name=input("enter your name :")
        self.course=input("enter your course :")
        self.subject=input("enter your subject :")
    def show(self):
        print("Name :",self.name)
        print("Course :",self.course)
        print("Subject:",self.subject)
s1=student()
s1.show()

