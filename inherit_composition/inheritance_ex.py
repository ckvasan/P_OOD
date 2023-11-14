from abc import ABC, abstractmethod
class HumanAsset (ABC) :
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def orgassocited(self):
        return "BOSCH"


    @abstractmethod
    def natureofwork(self):
        pass

class invester (HumanAsset):
    def __init__(self, id , name , role , share):
        super().__init__(id,name,role)
        self.share = share

    def natureofwork(self):
        return f"{self.orgassocited()} Invester monitoring P&L of org"
class employee(HumanAsset):
    def __init__(self, id ,name,role,salary):
        super().__init__(id, name,role)
        self.salary = salary

    def natureofwork(self):
        return f"{self.orgassocited()} Employee doing Project Delivery"



class contractor(employee):
    def __init__(self, id ,name,role,salary):
        super().__init__(id, name,role,salary)


    def orgassocited(self):
        return f"Contractor_Itemis"

e =  employee(1,"Keerthi","dev",199000)
i = invester(1001,"Anil","Independent Director",50)
print(i.__getattribute__("share"))
print (i.__getattribute__("name"))
print(e.__getattribute__("salary"))
print(e.__getattribute__("name"))
print(e.natureofwork())
print(i.natureofwork())
print(e.orgassocited())
print(i.orgassocited())

c= contractor('c001','Mark','Web dev',45000)
print(c.__getattribute__("salary"))
print (c.__getattribute__("name"))
print(c.orgassocited())
print(c.natureofwork())