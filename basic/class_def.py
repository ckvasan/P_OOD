class employee:
    PROJECTS = ('WEB', 'DEVOPS', 'TEST_AUTOMATION')

    GENDER = ('M','F','T')

    @classmethod
    def involvedprojects(cls):
        return cls.PROJECTS

    @staticmethod
    def org():
        return "BOSCH"

    def __init__(self, id, name, role, salary):
        self.id = id
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        return f'employee ({self.id}, {self.name}, {self.role})'

    def setbonus(self, bonus):
        self.__bonus = bonus

    def getrevisedsalary(self):
        self.salary += self.salary * self.__bonus
        return self.salary

    def __repr__(self):
        return f'''
        employee ( id = {self.id},
        name= {self.name},
        role = {self.role} )
        '''

class invester :

    def __init__(self, id, name, role, share):
        self.id = id
        self.name = name
        self.role = role
        self.share = share


if __name__ == '__main__':

    e = employee(1, "Keerthi", "Software Developer", 16000)
    e2= employee(2,"vasan","Data Scientist",20000)
    i = invester (1001,"Ambani","Partner",40)
    i2 = invester(1002,"Adani", "Director",25)



    e.setbonus(.25)
    print(e)
    print(repr(e))

    print(e.getrevisedsalary())
    print(employee.involvedprojects())

    print(e.org())

    print("object Type", type(e) is employee, sep= "***")
    print("object Type", type(i) is employee)
    print("object Type", type(i) is invester)
    print("Instance Type", isinstance(e,employee))
    print("Instance Type", isinstance(i, invester))
    print("Instance Type", isinstance(i2, employee))

    print("employee Type vs object by type()", type(e) is object)
    print("employee Type vs object by isinstance()", isinstance(e, object))
