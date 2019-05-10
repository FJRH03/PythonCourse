'''
    Author: @XXXKaos (GitHub)
    Francisco Ramirez
    Twitter: @DeNyJaviier
'''

#Python Object-Oriented Programming
class Employee:

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)
#Create and initialize objects in Pyhton

emp_1 = Employee('Francisco', 'Ramirez', 15000)
emp_2 = Employee('Javier', 'Hernandez', 26000)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
