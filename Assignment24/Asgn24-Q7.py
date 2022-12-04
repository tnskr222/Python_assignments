"""python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values)."""

class laptop:

    brand = 'Lenovo'
    ram = '8 GB'
    cpu = 'i5'
    hdd = '1TB'
    
    def __init__(self):
        self.brand = laptop.brand
        self.ram = laptop.ram
        self.cpu = laptop.cpu
        self.hdd = laptop.hdd

    def showConfig(self):
        print(self.brand, self.hdd, self.ram,self.cpu)

a =laptop()
a.showConfig()
