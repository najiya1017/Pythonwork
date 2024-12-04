#method overriding

class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*20)



class ExpressShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*20)


class StandardShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*5)


obj=ExpressShipping()

obj.calculate_shipping_cost(10)

obj2=StandardShipping()

obj2.calculate_shipping_cost(10)