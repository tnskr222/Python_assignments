# recursive python function to print octal of a given decimal number

a = int(input('Enter decimal number to print octal number : '))

def octal(a):
    if a >7:
        octal(a//8)
    print(a%8,end='')


octal(a)