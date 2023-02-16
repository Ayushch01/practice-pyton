class employee:
    def __init__(self):
        self.name=input("enter employees name :")
        self.employee_id=input("enter employees id :")
        self.address=input("address :")
        self.contact=input("contact no :")
        self.department=input("employee department :")

    def show_detail(self):
        print("employee Id :",self.employee_id)
        print("Employee Name :",self.name)
        print("Address :",self.address)
        print("Contact :",self.contact)
        print("employees department :",self.department)

    def dwrite(self):
        f=open("employee.txt","a")
        data=self.employee_id+","+self.name+","+self.contact+","+self.address+","+self.department+"\n"
        f.write(data)
        print("data entried successfully")

class manager(employee):
    # employee().__init__()

    def dep_employee_detail(self):
        f=open("employee.txt","r")
        data=f.read()
        data_row=data.split("\n")
        data_row.pop()
        valid_row=[]
        for i in data_row:
            x=i.split(",")
            if self.department == x[len(x)-1]:
                valid_row.append(i)
class owner(manager,employee):
    def show_all(self):
        f=open("employee.txt","r")
        data=f.read()
        data_row=data.split("\n")
        data_row.pop()
        for i in data_row:
            x=i.split(",")
            print("-------------------")
            print("employee id :",x[0])
            print("Name :",x[1])
            print("contact :",x[2])
            print("address :",x[3])
            print("department :",x[4])
            print("-------------------")
s1=employee()
s2=manager()
s3=owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()
s1.show_detail()
s2.show_detail()
s2.dep_employee_detail()
s3.show_detail()
s3.dep_employee_detail()
s3.show_all()