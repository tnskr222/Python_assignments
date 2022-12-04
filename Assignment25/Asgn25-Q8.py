# python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.

class Phone:

    def calling(self):
        c = 'calling'
        return c

    def sms(self):
        c = 'sms'
        return c

class Calculator:

    a = 8
    b = 2

    def multiply(cls):
        c = cls.a*cls.b
        return c

    def division(cls):
        c = cls.a//cls.b
        return c

class SmartPhone(Phone,Calculator):
    pass

a = SmartPhone()
print(a.multiply())
print(a.calling())