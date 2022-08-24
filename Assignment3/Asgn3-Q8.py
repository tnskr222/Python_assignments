# python script to store a hexadecimal number 2F in a variable and print it in octal format

a = 0x2F
b = oct(a)
print("octal equivalent of hexadecimal number", hex(a).replace('0x',''), 'is', oct(a).replace('0o',''))