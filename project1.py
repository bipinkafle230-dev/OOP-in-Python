#object-oriented Programming concepts

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")

#play 
# name=input("Enter the name:")
# age=int(input("Enter the age:"))
# salary=int(input("Enter the salary:"))
# emp1 = Employee(name, age , salary)

emp1=Employee("Bhim","56","1209090")


emp1.display()