# python script to update 2nd Question, change email and age to __email and __age.

# python script to update the above Profile class with encapsulation


class Profile:

    def __init__(self,name,email,age):
        self.name = name
        self.__email = email
        self.__age = age

    def get_age(self):
        return self.__age, self.__email

    def set_age(self,age,email):
       self.__age = age
       self.__email = email

a = Profile('suresh','abc@gmail.com',28)

print('Name', a.name, a.get_age())

a.set_age(24,'hello@gmail.com')

print('Name', a.name, a.get_age())