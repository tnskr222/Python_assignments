"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""

x = int(input("Enter number : "))

if x%2==0:
    print("Saurabh Shukla")
elif x%2!=0 and x<0:
    print("Prateek Jain")
elif x%2!=0 and x>0:
    print("Aditya Choudhary")