class Person:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age
    
    def change_age(self, new_age):
        self.age = new_age

class Department:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def change_name(self, new_name):
        self.name = new_name

class Employee(Person, Department):
    def __init__(self, salary, fname, age, name, id):
        Person.__init__(self, fname, age)
        Department.__init__(self, name, id)
        self.salary = salary
    
    def __repr__(self) -> str:
        return f"Name: {self.fname}\nAge: {self.age}\nDepartment: {self.name}\nId: {self.id}\nSalary: {self.salary}\n"

employee1 = Employee(1000, 'Bob', 23, 'Marketing', '234-cd-34')
employee2 = Employee(4000, 'Eldar', 30, 'Software Developer', '8978-e45v-r')

print(employee1)
print(employee2)
employee2.change_name('Coding Developer')
employee2.change_age(29)
print(employee2)