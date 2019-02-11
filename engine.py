import sqlite3
from os.path import exists

db_path = 'static/db/phonebook_database.db'

def main_p(surname, postcode, city):
    c = connect_db()
    if check_db() and connect_db():
        return get_person(c, surname, postcode, city)

    else:
        print('Error')

def main_b(biz_name, biz_type, postcode, city):
    c = connect_db()
    if check_db() and connect_db():
        return get_business(c, biz_name, biz_type, postcode, city)
    else:
        print('Error')

def check_db():
    if exists(db_path):
        return True
    else:
        return False

def connect_db():
    if check_db():
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            return c
        except Exception as e:
            print(e)
    else:
        print('Database error: path or connection')

def get_person(cursor, surname=None, postcode=None, city=None):
    surname = surname.title()
    if surname and postcode:
        postcode = postcode.upper()
        cursor.execute("SELECT * FROM phonebook_personal WHERE postcode LIKE ? and last_name = ? LIMIT 50", (postcode, surname,))

    elif surname and city:
        city = city.title()
        cursor.execute("SELECT * FROM phonebook_personal WHERE last_name = ? and addressline2 = ? LIMIT 50", (surname, city,))
    returned_results = cursor.fetchall()
    cursor.close()
    return isResultEmpty(returned_results)

def get_business(cursor, biz_name=None, biz_type=None, postcode=None, city=None):
    if city:
        city = city.title()
        if biz_type and city:
            biz_type = biz_type.title()
            cursor.execute("SELECT * FROM phonebook_business WHERE business_type = ? and addressline2 = ? LIMIT 50", (biz_type,city,))
        elif biz_name and city:
            biz_name = biz_name.title()
            print(biz_name,city)
            cursor.execute("SELECT * FROM phonebook_business WHERE business_name = ? and addressline2 = ? LIMIT 50", (biz_name, city,))
    elif postcode:
        postcode = postcode.upper()
        if biz_type and postcode:
            biz_type = biz_type.title()  
            cursor.execute("SELECT * FROM phonebook_business WHERE business_type = ? and postcode = ? LIMIT 50", (biz_type, postcode,))
        elif biz_name and postcode:
            biz_name = biz_name.title()    
            cursor.execute("SELECT * FROM phonebook_business WHERE business_name = ? and postcode = ? LIMIT 50", (biz_name, postcode,))

    returned_results = cursor.fetchall()
    cursor.close()
    return isResultEmpty(returned_results)

def format_results(returned_results):
    i = "\n".join([str(item) for item in returned_results])
    return i 

def isResultEmpty(returned_results):
    if returned_results == []:
        return returned_results
        # return 'Nth in db'
    else:
        format_results(returned_results)
        return returned_results



        
