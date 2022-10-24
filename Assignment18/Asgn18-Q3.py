# python program to get a list of the values from a dictionary.

Info = dict(name ='Suresh', Age =22, Gender = 'Male', Experience = '1 Year')
a = []
for i in Info:
    a.append(Info[i])
print(a)