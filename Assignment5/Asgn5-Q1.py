# python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)

a = int(input("Enter a number"))
print(int(str(a)[:-1]))
print(round(a/10))