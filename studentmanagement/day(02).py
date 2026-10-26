
class Student:

    def __init__(self, name, id, marks):
       self.name = name
       self.id = id
       self.marks = marks

    def sutdents_marks(self):

        if self.marks >= 80:
           print('GRADE A+')
        elif self.marks >= 70 :
           print('GRADE A ')
        elif self.marks >= 60 :
           print('GRADE B+')
        elif self.marks >= 50:
           print('GRADE C+')
        elif self.marks >= 40 :
           print('GRADE D+')
        else :
           print('GRADE F')

    def check_result(self):
       if self.marks >= 40:
           print("Pass")
       else:
           print("Fail")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
                print("Invalid input! please enter an integer number:")


student1 = []
for i in range(1, 4):

    name = input(f"Enter student {i} name: ")
    id = get_int(f"Enter student {i} ID: ")
    marks = get_int(f"Enter student {i} marks: ")

    student1.append(Student(name, id, marks))

print()

for s in student1:

    print(s.name)
    print(s.id)
    print(s.marks)
    s.sutdents_marks()
    s.check_result()
    print()

def calculate_average(students):
    average = sum(s.marks for s in students) / len(students)
    print(average)
calculate_average(student1)