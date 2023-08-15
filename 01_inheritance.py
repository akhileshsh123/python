class Employee:
    company = "Google"


def showDetails(self):
    print("This is an employee")


class Programmer(Employee):
    language = "Python"


def getLanuage(self):
    print(f"The lanuage is {self.lanuage}")


def showDetails(self):
    print("This is an programmer")

e = Employee()
e.showdetails()
p = Programmer()
p.showDetails()
print(p.company)
