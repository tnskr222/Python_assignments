# python program to init default values for user object using __init__ method.

class user:

    def __init__(self):
        self.marks = 10
        self.mail = 'abc@suresh.com'

    def get_mail(self):
        return self.mail

a = user()
print(a.marks)
print(a.mail)
print(a.get_mail())