class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit_money(self, amount):

        if amount > 0:
            self.balance += amount
            print("deposit successfully done")
        else:
            print("deposit is not done succefully")

    def withdraw_money(self, amount):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print('withdraw successfull')
        else:
            pint("withdraw is no successfull")

    def check_balance(self):
        print(f'the current balance is{self.balance}')


value = Bankaccount('shamim', 5000)

value.deposit_money(1000)
value.check_balance()

value.withdraw_money(2000)
value.check_balance()