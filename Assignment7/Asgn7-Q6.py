# python program to check whether a given string is a multiword string or single word string using match case statement

x = input("Enter input : ")
if " " in x:
    y = 1
else:
    y=2

match y:
    case 1:
        print("Given input is multi word string")
    case 2:
        print("Given input is single word string")