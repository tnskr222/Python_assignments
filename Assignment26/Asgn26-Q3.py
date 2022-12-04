"""python script to create a to print the above user account object using operator
overloading (hint __str__ method)"""

class user:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other1):
        total_m1 = self.m1+other1.m1
        total_m2 = self.m2+other1.m2
        s4 = user(total_m1,total_m2)
        return s4

    def __str__(self):
        return str(self.m1)+':'+str(self.m2)

a = user('123s',5800)
b = user('124r', 1000)
c = user('564g',2000)
d = a+b+c

print(d)