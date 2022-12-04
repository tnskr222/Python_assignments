# program to delete the age property of the user.

class user:

    def __init__(self):
        self.name = 'suresh'
        self.age = 27

    def myname(self):
        return self.name

    def myage(self):
        return self.age

a = user()

print(a.myname())
print(a.myage())
del a.myage
print(a.myage())