class bank:

    accno:int

    balance:int

    ac_type:str

    name:str

    def __init__(self,accnt,blnce,types,name):

        self.accno=accnt

        self.balance=blnce

        self.ac_type=types

        self.name=name

    def deposit(self,amount):

        self.balance+=amount

        print(f"your Account{self.accno} is credited with amount {amount}.Your avl balance {self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            print("Insufficient Balnce")

        else:

            self.balance-=amount

            print(f"your Account{self.accno} is debited with amount {amount}.Your avl balance {self.balance}")


    def get_balance(self):

        print("Your avl balance:",self.balance)

bank_instance=bank(71010102133,50000,"savings","rahul")

bank_instance.deposit(10000)

bank_instance.withdraw(20000)

bank_instance.get_balance()

bank_instance.withdraw(200000)