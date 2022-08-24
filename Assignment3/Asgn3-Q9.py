# python script to store an octal number 125 in a variable and print it in binary format
a = 0o125
print('binary format of octal number', oct(a).replace('0o',''), 'is', bin(a).replace('0b',''))