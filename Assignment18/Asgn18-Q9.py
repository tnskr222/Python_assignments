# python program to merge two python dictionaries into one dictionary.

Person = {'name':'Suresh', 'Age' :22, 'Gender' : 'Male'}
Study = {'SSC':90.6, 'Diploma':86.2, 'Graduation':85.6, 'PG':80}
for i in Study:
    Person[i]=Study[i]
print(Person)