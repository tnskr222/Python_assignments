# python program to create 3 user objects and find the youngest of all.

class user:

    def youngest(self,a,b,c):
        if a<b and a<c:
            print('a is the youngest')
        elif b<a and b<c:
            print('b is the youngest')
        else:
            print('c is the youngest')

d = user()
d.youngest(100,9,6)