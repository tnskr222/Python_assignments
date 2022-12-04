# python script to update the above Profile class with encapsulation


class Profile:

    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.__age = age

    # def get_age(self):
    #     return self.__age

    # def set_age(self,age):
    #    self.__age = age

a = Profile('suresh','abc@gmail.com',28)

print('Name', a.name, a.__age, a.email)

# a.set_age(24)

# print('Name', a.name, a.get_age(), a.email)