# python script to print two given words in dictionary order

x = input("Enter first word ")
y = input("Enter second word ")
if x<y:
    print(x,y,sep='\n')
elif x>y:
    print(y,x,sep='\n')
else:
    print(x)