# python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist.insert(thislist.index("SQL"), "NOSQL")
thislist.insert(thislist.index("Reactnative"), "Flutter")
thislist.remove("Reactnative")
thislist.remove("SQL")
print(thislist)