""" python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"} """

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}

for i in secondset:
    thisset.add(i)
print(thisset)