class mobile():

    name:str

    price:int

    brand:str

    def __init__(self,name,price,brand):

        self.name=name

        self.price=price

        self.brand=brand

    def display(self):

        print(self.name,self.brand,self.price)

mobile_inst=mobile("oneplusnord9r",45000,"oneplus")

mobile_inst.display()