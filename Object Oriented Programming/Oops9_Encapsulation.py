class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Now Balance is:",self.balance)

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"is credited in your account")
        print("Now Balance is:",self.balance)

a1=Account(10000,"12abcd12")
a1.debit(500)
a1.credit(5000)