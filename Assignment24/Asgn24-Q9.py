# python program to create a School class and 3 instance variables and 1 class variable.

class School:

    school_name = 'ineuron'

    def __init__(self,name,age,language):
        self.name = name
        self.age = age
        self.language = language
a = School('suresh',28,'python')
print(a.school_name)
print(a.name, a.age, a.language)