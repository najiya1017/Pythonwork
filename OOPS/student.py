class student:

    rollnumber:int

    name:str

    course:str

    def set_student(self,id1,name,course):

        self.name=name

        self.rollnumber=id1

        self.course=course

    def display_student(self):

        print(f"{self.rollnumber},{self.name},{self.course}")

obj=student()

obj.set_student(10,"vaishnav","python")

obj.display_student()

#employyee,student