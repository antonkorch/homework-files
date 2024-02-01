import psycopg2
import configparser

def create_table(cursor, table_name):
    cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
    cursor.execute('''CREATE TABLE {} 
                    (id serial PRIMARY KEY, name VARCHAR(40) NOT NULL, surname VARCHAR(40) NOT NULL, 
                    email VARCHAR(40) NOT NULL, telephones TEXT[]);'''.format(table_name))
    
def add_client(cursor, table_name, name, surname, email, telephones):
    tel_str = '{' + ','.join(telephones) + '}'
    cursor.execute('''INSERT INTO {} (name, surname, email, telephones) 
                    VALUES (%s, %s, %s, %s)'''.format(table_name), (name, surname, email, tel_str))

def add_telephone(cursor, table_name, email, telephone):
    cursor.execute('''UPDATE {} SET telephones = telephones || %s 
                        WHERE email = %s'''.format(table_name), (telephone, email))

def change_data(cursor, table_name, id, new_name, new_surname, new_email):
    cursor.execute('''UPDATE {} SET name = %s, surname = %s, email = %s
                        WHERE id = %s'''.format(table_name), 
                        (new_name, new_surname, new_email, id))

def delete_telephone(cursor, table_name, email, telephone):
    cursor.execute('''UPDATE {} SET telephones = array_remove(telephones, %s) 
                        WHERE email = %s'''.format(table_name), (telephone, email))

def delete_client(cursor, table_name, id):
    cursor.execute('''DELETE FROM {} WHERE id = %s'''.format(table_name), (id,))

def get_client(cursor, table_name, id):
    cursor.execute('''SELECT * FROM {} WHERE id = %s'''.format(table_name), (id,))
    return cursor.fetchone()

config = configparser.ConfigParser()
config.read('settings.ini')

database = "05-psycopg"
user =  (config['LOGIN']['user'])
password = (config['LOGIN']['password'])

conn = psycopg2.connect(database=database, user=user, password=password)
with conn.cursor() as cur:
    #create a table
    create_table(cur, 'clients')
    
    #add a client
    add_client  (cur, 'clients', 'John', 'Deer', 'john@deer.com', 
                ['+1 999 876 5432', '+1 999 123 4567'])
    
    #add a telephone to existing client
    add_telephone(cur, 'clients', 'john@deer.com', "{+1 999 000 0000}")

    #change data of a client
    change_data(cur, 'clients', 1, 'John', 'Deere', 'john@is_not_a_deer.com')

    #delete a telephone from a client
    delete_telephone(cur, 'clients', 'john@is_not_a_deer.com', '+1 999 876 5432')

    #delete a client
    delete_client(cur, 'clients', 1)

    #add a client again
    add_client  (cur, 'clients', 'John', 'Deer', 'john@deer.com', 
                ['+1 999 876 5432', '+1 999 123 4567'])
    
    #get s client info
    client = get_client(cur, 'clients', 2)
    print(client)


    conn.commit()
conn.close()