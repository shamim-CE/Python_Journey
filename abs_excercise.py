from  abc import ABC, abstractmethod

class payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass
class CreditCard(payment):
    def __init__(self, card_num, amount):
        self.card_num = card_num
        self.amount = amount

    def process_payment(self):
       print(f'the payment id is {self.card_num} and the amount is {self.amount} ')
class MobileBanking(payment):
    def __init__(self, phone_num, amount):
        self.phone_num = phone_num
        self.amount = amount

    def process_payment(self):
        print(f'the payment phone number is {self.phone_num} and the amount is  {self.amount} ')
class Bank_Transfer(payment):
    def __init__(self, acc_num, amount):
        self.acc_num = acc_num
        self.amount = amount
    def process_payment(self):
        print(f'the payment account number is {self.acc_num} and the amount is {self.amount} ')
three_trasaction = [CreditCard(123,20000), MobileBanking(132,10000),Bank_Transfer(222,30000)]

for shamim in three_trasaction:
  shamim.process_payment()