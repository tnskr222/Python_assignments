"""Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file """


file = open("file.txt","wt")
file.write("I am student")
print("Name of the File : ",file.name)

print("Closed or Not    : ",file.closed)

print("Opening Mode     : ",file.mode)


file.close()

print("")

print("Closed or Not    : ",file.closed)