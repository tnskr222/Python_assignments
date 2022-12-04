"""python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry)"""

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

d = Truecaller()

print(d.fetch(987634))

print(d.entry(965874,'bharat'))