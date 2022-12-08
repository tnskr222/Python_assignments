# Python script to create a new file ‘myfile.txt’ and store user entered text.

file = open("myfile.txt","r")
file.write(input("Enter text : "))
file.close()