class Employee:
    def __init__(self, empid = None, name = None, salary = None):
        self.empid = empid
        self.name = name
        self.salary = salary
    def setempid(self, empid):
        self.empid = empid
    def setname(self, name):
        self.name = name
    def setsalary(self, salary):
        self.salary = salary
    def getempid(self):
        return self.empid
    def getempname(self):
        return self.name
    def getempsalary(self):
        return self.salary
    
e1 = Employee()
e2 = Employee(1, "Shantunu", 50000)
e1.setempid(2)
e1.setname("Rahul")
e1.setsalary(40000)
print(e1.getempid(), e1.getempname(), e1.getempsalary())
print(e2.getempid(), e2.getempname(), e2.getempsalary())