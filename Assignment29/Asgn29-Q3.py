# Python script to read the above created file ‘myfile.txt’ and display content on the console.

f  = open("cities.txt","r")
print(f.read())
f.close()