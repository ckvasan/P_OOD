'''
Multiple Inheritance
'''
class employee :
    def __init__(self,name):
        self.name = name

    def setorg(self,org):
        self.org = org
    def natureofwork(self):
        return f'{self.name} is developer at {self.org}'

class trainer :

    def ___init__(self,name):
        self.name = name

    def settopics (self, topics):
        self.topics = topics
    def setacademy(self, academy):
        self.academy = academy
    def trains(self):
        return f'{self.name} is trainer at {self.academy}, trains on {tuple([t for t in self.topics])}'

class specialist (employee,trainer) :

    def __init__(self,name,org,academy,topics):
        super().__init__(name)
        super().setorg(org)
        super().setacademy(academy)
        super().settopics(topics)


s = specialist('Mike','BOSCH','leetcode',('python','java'))
print(s.natureofwork())
print(s.trains())