import random


class employee:
    def __init__(self, id, name, role, salary):
        super().__init__()
        self.__call__(id, name, role, salary)

    def __setattr__(self, key, value):
        if (key == 'hike'):
            try:
                if (value < 0.1):
                    raise ValueError
            except ValueError as v:
                print("The minimum hike is 10%")
                value = 0.1
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        if item == 'salary':
            sal = super().__getattribute__('salary')
            hik = super().__getattribute__('hike')
            self.salary = sal + (sal * hik)
        return super().__getattribute__(item)

    def __eq__(self, other):
        if not isinstance(other, employee):
            raise ValueError("Comparing object should of same type")
        return self.id == other.id;

    def __ge__(self, other):
        if not isinstance(other, employee):
            raise ValueError("Comparing object should of same type")
        return self.id >= other.id;

    def __lt__(self, other):
        if not isinstance(other, employee):
            raise ValueError("Comparing object should of same type")
        return self.id < other.id;

    def __getattr__(self, item):
        if item == 'salary':
            return super().__getattribute__("salary") * 1.1
        return super().__getattr__(item)

    def __call__(self, id, name, role, salary):
        self.id = id
        self.name = name
        self.role = role
        self.salary = salary


e = employee(123, "Mike", "expert", 15000)
print(e.id)
print(e.name)
e.hike = 0.30
print(e.role)
print(e.salary)

# Mike had a name changed to Micheal, got promoted with increase in salary, notice : empid is same
e(123, 'Micheal', 'Manger', 18900)
print(e.id)
print(e.name)
e.hike = 0.30
print(e.role)
print(e.salary)

e1 = employee(123, "Tim", "dev", 15600)

if e == e1:
    print(
        f"Both {e.name} and {e1.name} have same employee id : !!! ERROR : Synchronization Issue !!!, System should correct the employee ID")
    print("Fixing the isssue....")
    v = random.randint(1, 10)
    if (v > 5):
        print(f"Random Number {v}")
        e1(345, "Tim", "dev", 450)
    else:
        print(f"Random Number {v}")
        e1(100, "Tim", "dev", 45088)

if (e > e1):
    print(f"{e.name} joined later {e1.name} in the org")

elif (e < e1):
    print(f"{e.name} joined before {e1.name} in the org")
else:
    print("!!!!!!!STRANGE ERROR !!!!!!!!!!!!!!!!!!")
