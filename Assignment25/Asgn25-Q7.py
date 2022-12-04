# python script to create a Phone class with 2 methods to print the features (calling and sms).

class Phone:

    def calling(self):
        c = 'calling'
        return c

    def sms(self):
        c = 'sms'
        return c

a = Phone()
print(a.calling())

print(a.sms())