class Bank:

    name:str

    mpin:int

    accnt_type:str

    balance:int


    def __init__(self,name,mpin,accnt_type,balance):

        self.name=name

        self.__mpin=mpin

        self.accnt_type=accnt_type

        self.__balance=balance


    def get_balance(self):

        print(self.__balance)


obj=Bank("Hari",2345,"saving",45000)

# print(obj.__balance)

obj.get_balance()