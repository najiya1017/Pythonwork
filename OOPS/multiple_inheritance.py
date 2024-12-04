class Person:

    name:str

    age:int

    def __init__(self,name,age):

        self.name=name

        self.age=age

    def display_person_info(self):

        print(self.name,self.age)



class Employee:

    emp_id:int

    salary:int

    def __init__(self,id,sal):

        self.emp_id=id

        self.salary=sal

    def display_emp_info(self):

        print(self.emp_id,self.salary)



class Manager(Employee,Person):

    department:str

    def __init__(self,name,age,eid,sal,dept):

        Person.__init__(self,name,age)

        Employee.__init__(self,eid,sal)

        self.department=dept

    def display_manager_info(self):

        self.display_person_info()

        self.display_emp_info()

        print(self.department)




m_instance=Manager("hari",32,123,25000,"Developer")

m_instance.display_manager_info()