# python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)

a = int(input("Enter number "))
last_digit = int(str(a)[-1])
print(f"The last digit of {a} is {last_digit}")