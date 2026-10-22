from abc import ABC, abstractmethod
class payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class Bkash(payment):
    def pay(self,amount):
        print(f'paid {amount} using BKASH ')

class Card(payment):
    def pay(self,amount):
        print(f'paid {amount} using CARD ')

bkash = Bkash()
card = Card()
bkash.pay(100)
card.pay(200)


class CloudStorage:

    @abstractmethod
    def upload_file(self,file_name):
        pass

class S3Storage(CloudStorage):
    def upload_file(self,file_name):
        print(f'uploading {file_name} to aws s3')

class AzureStorage(CloudStorage):
    def upload_file(self,file_name):
        print(f'uploading {file_name} to azure')
s3 = S3Storage()
azure = AzureStorage()

s3.upload_file('csv')
azure.upload_file('json')




class Cloudresource(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass

class EC2(Cloudresource):
    def __init__(self,hours,hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_cost(self):
         total_rate =  self.hours * self.hourly_rate
         return total_rate

class S3(Cloudresource):
    def __init__(self,storage_gb,storage_cost_per_gb):
        self.storage_gb = storage_gb
        self.storage_cost_per_gb = storage_cost_per_gb

    def calculate_cost(self):
         total_gb  =  self.storage_gb * self.storage_cost_per_gb
         return total_gb

class RDS(Cloudresource):
    def __init__(self,hours,hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_cost(self):
        cost = self.hours * self.hourly_rate
        return cost

virtual  =  EC2(10,10)
storage =  S3(5,10)
data = RDS(5,10)




total_cost = [virtual, storage, data]
total = 0
for tot in total_cost:
  total += tot.calculate_cost()
print(total)