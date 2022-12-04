# python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.



class Profile:

    platform = 'python'

    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.__age = age

    def method(cls):
        return cls.platform 

a = Profile('suresh','abc@gmail.com',28)
print(a.method())