class student:
    def __init__(self):
        self.name=input("enter students name :")
        self.fathername=input("enter students fathers name :")
        self.age=input("enter age :")
        self.year=input("enter year :")
        self.course=input("enter course :")
        self.contact=input("enter contact :")
    def show_detail(self):
        print("Name :",self.name)
        print("Fathers name :",self.fathername)
        print("Age :",self.age)
        print("Year of joining :",self.year)
        print("course :",self.course)
        print("contact number :",self.contact)
def generate_rollno(self):