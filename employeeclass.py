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

    def write(self):
        f=open("employee.txt","a")
        data=self.employee_id+"\n"+self.name+"\n"+self.contact+"\n"+self.address+"\n"+self.department+"\n"
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
