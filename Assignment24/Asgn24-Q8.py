"""WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size."""

class laptop:

    brand = 'Lenovo'
    ram = '8 GB'
    cpu = 'i5'
    hdd = '1TB'
    
    # def __init__(self,brand,ram,cpu,hdd):
    #     self.brand = brand
    #     self.ram = ram
    #     self.cpu = cpu
    #     self.hdd = hdd
        

    def lap_list(f,g,h,i):
        # f= self.brand
        # g = self.ram
        # h = self.cpu
        # i = self.hdd
        e = []
        e.append(f)
        e.append(g)
        e.append(h)
        e.append(i)
        return e

def sort_list(d):
    return(sorted(d, key = lambda x:x[1]))

a =laptop.lap_list('lenovo',4, 'i3','1TB')
print(a, type(a))
b =laptop.lap_list('hp',26, 'i5','3TB')
c =laptop.lap_list('dell',16, 'i7','2TB')

d=[]
d.append(a)
d.append(b)
d.append(c)

print(d)

print(sort_list(d))