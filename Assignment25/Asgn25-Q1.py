#python script to create a Profile class with 3 attributes (name, email, age)

class Profile:
    Student_name = 'suresh'

    def __init__(self,email,age):
        self.email = email
        self.age =age

a = Profile('abc@gmail.com',28)
b = Profile('hello@gmail.com',27)

print(a.Student_name)