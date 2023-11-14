from dataclasses import dataclass,field


@dataclass
class book :

    name:str
    author: str
    page: int
    price : float


    def __post_init__(self):
        self.description = self.__aboutbook()
    def __aboutbook(self):
        return f"Book named {self.name} authored by {self.author}, contains {self.page} and cost is {self.price}"
    def getdesc(self):
        return self.description
    @staticmethod
    def publication():
        return "Oxford Publication"

b = book("python programming","Guido",400,1989)
b1= book("python programming","Guido",400,1989)
b2= book("python programming 2","Guido",405,1989)
print(b)
print(b.getdesc())
print(b.publication())
print (b == b1)
print(b == b2)

print ("**********************************************************************")
@dataclass
class defbook:
       name : str = "python pramming"
       author:str ="guido"
       price :float = field(default="2899.0")

df = defbook ();
df2 = defbook("python pramming","guido","2899.0")
df3 = defbook("python pramming vol2","guido","2809.0")
print (df)
print (df2)
print (df3)
print (df == df2)
print (df == df3)

print ("#################################################################")
@dataclass
class pybook:
    author :str
    pages :int
    price : float
    name : str = field(default = "python programming")

p = pybook("Guido",190,3458.7)
p1 = pybook("Rossman",679,7889.2)
p2 = pybook("Mike",69,789.2,"Advanced python programming")
p3 = pybook("Mike",69,789.2,"Advanced python programming")

print (p)
print (p1)
print(p2)
print (p == p1)
print(p3 == p2)
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

import random


def price():
    return float(random.randrange(300, 350))
@dataclass
class pgbook:
    author :str
    pages :int
    price : float = field(default_factory=price)
    name : str = field(default = "JAVA programming")


pg = pgbook("Scott",190)
pg1 = pgbook("Kolb",679)
pg2 = pgbook("Mike",69,789.2,"Advanced python programming")
pg3 = pgbook("Mike",69,789.2,"Advanced python programming")

print (pg)
print (pg1)
print(pg2)
print (pg == pg1)
print(pg3 == pg2)