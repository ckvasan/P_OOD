from abc import ABC, abstractmethod


class intro(ABC):
    @abstractmethod
    def aboutme(self):
        pass


class student(intro):
    def __init__(self, id, name, standard, rank):
        self.id = id
        self.name = name
        self.std = standard
        self.rank = rank

    def aboutme(self):
        return f"Hello all, I am {self.name}, studying {self.std} in {self.school}, I have scored rank- {self.rank}"


s = student(1, "Nalan", "2-D", 2)
s.__setattr__("school","Suguna PIP School")
print(s.aboutme())
