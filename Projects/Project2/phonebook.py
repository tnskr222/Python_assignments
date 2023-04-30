import psycopg2

import project2

try:
    conn=psycopg2.connect(
        database='postgres', user='postgres', password='postgres', host='127.0.0.1', port='5432'
    )
    conn.autocommit=True
except Exception as e:
    print(e)

cursor=conn.cursor()

# cursor.execute('select * from courses')

# data=cursor.fetchone()
# print(data)
try:
    login_signup=int(input("Press 1 and Enter for signup"+'\n'+'Press 2 and Enter for login'))
except Exception as e:
    print(e)
    exit()




if login_signup==1 or login_signup==2:
    email=input('Enter email :')
    password=input('Enter password :')
    if login_signup==1:
        project2.phonebook_auth(cursor,email,password)
        exit()
    else:
        login_check=project2.phonebook_auth_check(cursor,email,password)
else:
    print('Enter correct input')
    exit()

if login_check==1:
    # project2.insert_contact(cursor,email)
    project2.login_work(cursor,email)
    
conn.close()


