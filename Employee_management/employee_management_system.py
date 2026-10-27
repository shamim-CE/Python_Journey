
class Employee:
    def __init__(self,name,salary,overtime_hours):
        self.name = name
        self.salary = salary
        self.overtime_hours = overtime_hours

    def final_salary(self):
        if self.overtime_hours >= 1 :
           overtime = self.overtime_hours * 200
           return overtime
        else:
            overtime = 0
            return overtime

    def bonus_salary(self):
        if self.salary > 30000:
           bonus =  self.salary * 0.10
           return bonus
        else:
           bonus = 0
           return bonus


    def total_salary(self):
        total_salary = self.salary  + self.final_salary()+ self.bonus_salary()
        return total_salary

def check(prompt):
    while True:
        try:
            return int(input(prompt))


        except ValueError:
            print("Please enter a number")

employee = []

for n in  range(5):
    name = input("Enter employee name: ")
    salary = check("enter the salary: ")
    overtime_hours = check("enter the overtime hours: ")
    employee.append(Employee(name,salary,overtime_hours))

print()
for result in employee:
    print('name:',result.name)
    print('salary:',result.salary)
    print('over time hours:',result.overtime_hours)
    print('bonus amount:',result.bonus_salary())
    print('overtime bonus:',result.final_salary())
    print('total salary:',result.total_salary())
