# python program to create 2 objects of the user class and assign different values.

class user:

    myname = "suresh"
    def name(cls):
        return cls.myname

    def age(self):
        print("my age is : 27")

b = user()
print("My name is : ",b.name())
b.age()