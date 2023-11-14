
import abc
class vehicle(abc.ABC) :
    '''

Multilevel iheritance
'''
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model

    @abc.abstractmethod
    def purposeofuse(self):
        pass

    @abc.abstractmethod
    def fuel(self):
        pass

class car(vehicle):

    def __init__(self, brand,model,variant):
        super().__init__(brand,model)
        self.variant = variant

    def purposeofuse(self):
        return "Passenger Cars"


class mpv(car):

    def __init__(self, brand,model,variant,seats):
        super().__init__(brand,model,variant)
        self.seats = seats


    def typeofvehicle(self): #str
        return f"{self.brand} --- {self.model} --- {self.variant}-- {self.seats}"

    def fuel(self):
        return "Electric"

m = mpv('Volvo','MP90','AX',7)
print(m.fuel())
print(m.typeofvehicle())
print(m.purposeofuse())