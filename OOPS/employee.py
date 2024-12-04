class employee:

    empid:int

    name:str

    department:str

    def set_employee(self,id1,name,dept):

        self.name=name

        self.empid=id1

        self.department=dept

    def display_emp(self):

        print(f"{self.empid},{self.name},{self.department}")

obj=employee()

obj.set_employee(10,"vaishnav","python")

obj.display_emp()

#employyee,student