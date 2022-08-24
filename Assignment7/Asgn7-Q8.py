"""python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""

a = input("Enter first string : ")
c = input("Enter second string : ")

if a==c:
    b=1
elif a<c:
    b=2
else:
    b=3

match b:
    case 1:
        print("Strings are identical")
    case 2:
        print("First string comes before second string")
    case 3:
        print("First string comes after second string")