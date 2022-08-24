"""program to display day name on the basis of user's liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""

a = input("Enter favourite colour ")

if "yellow" in a:
    b=1
elif "blue" in a:
    b=2
elif "orange" in a:
    b=3
elif "white" in a:
    b=4
elif "black" in a:
    b=5
elif "red" in a:
    b=6
else:
    b=7


match b:
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")