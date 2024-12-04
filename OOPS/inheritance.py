class parent:
    def vehicle(self):

        print("parent class ertiga vehicle")
class child(parent):

    pass

child_instance1=child()
child_instance1.vehicle()


#types of inheritance

#multiple inheritance

class Grandparent:

    def m1(self):

        print("Grand parent class m3 method. ")

class Parent:

    def m2(self):

        print("parent class m2 method.")

class Child(Parent,Grandparent):

    def m3(self):

        print("parent class m3 method.")

child_instance=Child()

child_instance.m3()

child_instance.m2()

child_instance.m2()

print("==============================================")

#multilevel inheritance

class Grandparent:

    def m1(self):

        print("Grand parent class m3 method. ")

class Parent(Grandparent):

    def m2(self):

        print("parent class m2 method.")

class Child(Parent):

    def m3(self):

        print("parent class m3 method.")

child_instance=Child()

child_instance.m3()

child_instance.m2()

child_instance.m2()

print("==============================================")


class Grandparent:

    def m(self):

        print("Grand parent class m method. ")

class Parent:

    def m(self):

        print("parent class m method.")

class Child(Parent,Grandparent):

    def m3(self):

        print("parent class m3 method.")

child_instance=Child()

child_instance.m3()

child_instance.m()

# child_instance.m2()