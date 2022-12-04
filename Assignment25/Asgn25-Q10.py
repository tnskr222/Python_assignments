"""python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller"""

class Truecaller:

    a =[[819875,'suresh'],[987634, 'harish'],[879632,'ramesh'],[956734,'ramana']]

    def fetch(cls,b):
        for i in cls.a:
            if i[0]==b:
                return i[1]

    def entry(cls,number,name):
        c =[number,name]
        cls.a.append(c)
        return cls.a

    def newmethod(self):
        d = Truecaller()
        return d.fetch(int(input('Enter number')))

b = Truecaller()

print(b.newmethod())