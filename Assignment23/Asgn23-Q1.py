# Use iter and next method to access all the elements of a given set using while loop

a = {1, 2, "suresh", "ineuron", "student"}

def iterandnext(a):
    b = iter(a)
    c = len(a)
    while c:
        d = next(b)
        print(d)
        c-=1

iterandnext(a)