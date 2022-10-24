# python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

from collections import ChainMap
Person = {'name':'Suresh', 'Age' :22, 'Gender' : 'Male'}
Study = {'SSC':90.6, 'Diploma':86.2, 'Graduation':85.6, 'PG':80}
Skills = {'Cloud':'Azure', 'Languages': 'Python', 'Tools':'Postman'}

Details = ChainMap(Person, Study, Skills)

print(Details)