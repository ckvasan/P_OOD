class employee:
    def __init__(self,id,name,role,proj,org):
        self.id = id
        self.name= name
        self.role = role
        self.proj = proj
        self.org = org

    def __str__(self):
        return f'''
                Hi, am {self.name} and employee id is {self.id} and role is {self.role},
                I am handling projects and details are {self.proj} in {self.org}
                '''


class project:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'[ID : {self.id} , Name: {self.name}]'
class org:
    def __init__(self, name,hq):

        self.name = name
        self.hq = hq

    def __str__(self):
        return f' {self.name}, which is headquatered at {self.hq}'

o = org("Bosch","Germany")
p = project("P123","Human_AI")
e = employee("E123","Keerthi","Project Lead",p,o)
print(e)