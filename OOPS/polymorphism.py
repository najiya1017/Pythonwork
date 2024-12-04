#method overloadng is n"t supported in python

#method overriding

class parent:

    def mobile(self):

        print("NokiaX2")


class child(parent):

    def mobile(self):

        print("iphone")


obj=child()

obj.mobile()