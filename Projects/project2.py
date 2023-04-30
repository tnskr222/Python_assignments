

import psycopg2

def phonebook_auth(cursor,email,password):
    cursor.execute(f"select email from phonebook_contacts_auth where email='{email}'")
    email_check=cursor.fetchall()
    print(len(email_check))
    if len(email_check)!=0:
        print('User allready exists')
    else:
        cursor.execute(f"Insert into phonebook_contacts_auth(email,password) values('{email}','{password}')")
        print('succesfully registered')

def phonebook_auth_check(cursor,email,password):
       cursor.execute(f"select password from phonebook_contacts_auth where email='{email}'")
       email_auth_check=cursor.fetchall()
    #    print(len(email_auth_check))
       if len(email_auth_check)==0:
            print('User not Register please Register')
            exit()
       elif len(email_auth_check)==1:
            for r,row in enumerate(email_auth_check):
                for c, col in enumerate(row):
                    if col==password:
                        print('Successfully logged in')
                        return 1
                    else:
                        print('Password doesn\'t match')
                        exit()
       elif len(email_auth_check)>1:
             print('Something Went Wrong')
             exit()
       
        


def insert_contact(cursor,email):
    contact_name=input("Enter Contact Name : ")
    contact_number=input("Enter Contact Number : ")
    try:
        cursor.execute(f"Insert into phonebook_contacts(contact_name,contact_number,email) values('{contact_name}','{contact_number}','{email}')")
        print('succesfully Inserted')
        login_work(cursor,email)
    except psycopg2.IntegrityError:
         print('Contact Number already exists')
         login_work(cursor,email)
    except Exception as e:
         print(e)
    
def update_contact(cursor,email):
    contact_name=input("Enter Contact Name : ")
    contact_number=input("Enter Contact Number : ")
    try:
        cursor.execute(f"Update phonebook_contacts set contact_number={contact_number} where contact_name='{contact_name}' and email='{email}'")
        print('succesfully Updated')
        login_work(cursor,email)
    except Exception as e:
         print(e)

def delete_contact(cursor,email):
    contact_name=input("Enter Contact Name : ")
    contact_number=input("Enter Contact Number : ")
    try:
        cursor.execute(f"Delete from phonebook_contacts where contact_name='{contact_name}' and contact_number='{contact_number}' and email='{email}'")
        print('succesfully Deleted')
        login_work(cursor,email)
    except Exception as e:
         print(e)   

def show_contact(cursor,email):
    try:
        cursor.execute(f"Select contact_name, contact_number from phonebook_contacts where email='{email}'")
        show_contacts=cursor.fetchall()
        print(show_contacts)
        login_work(cursor,email)
    except Exception as e:
         print(e)   

def login_work(cursor,email):
        login_work=int(input('Press 1 and Enter to insert new contact'+'\n'+'Press 2 and enter to update contact'+'\n'+'Press 3 and Enter to delete contact'+'\n'+'Press 4 and Enter to show all user contacts'+'\n'+'Press 0 to logout'))
        if login_work==1:
            insert_contact(cursor,email)
        elif login_work==2:
            update_contact(cursor,email)
        elif login_work==3:
            delete_contact(cursor,email)
        elif login_work==4:
            show_contact(cursor,email)
        elif login_work==0:
            exit()
        else:
            print('wrong input')
            login_work(cursor,email)