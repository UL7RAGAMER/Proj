import mysql.connector as s
from mysql.connector import errorcode
database_name = 'quiz'

conn=s.connect(host="localhost",user='root',passwd="2721")
b=True
if b:
    c = conn.cursor()
    c.execute('drop database quiz')


def create_sql_db():

    try:        
        cursor = conn.cursor()

        # Check if database exists
        cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = cursor.fetchone()

        if result:
            print(f"Database '{database_name}' already exists.")
        else:
            # Create the database
            cursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Database '{database_name}' created successfully.")
    except s.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    
    

class Quiz:

    def __init__ (self):
        self.admin_u="1"
        self.admin_p="2"
        self.categories = [] ; list
        
    def login(self):
        user=input("Do you want to login as a admin or player: ")
        while True:
            if user == 'asd':
                ad_user=input("Enter your admin username: ")
                ad_pass=input("Enter your admin pass: ")
            if ad_user==self.admin_u and ad_pass==self.admin_p:
                print("Welcome adm07!")
                break
            else:
                print("Wrong user or password try again")


    def category(self):
        cat = int(input("Enter the no of categories: "))
        for i in range(cat):
            n = input(f'Enter name of the category {i+1}:  ')
            q = []
            a = []
            qa = (n,q,a)
            self.categories.append(qa)  
        pass

    def create_tables(self):
        database_name = 'quiz'

        conn=s.connect(host="localhost",user='root',passwd="2721",database = database_name)
        
        for i in self.categories:
            a=0
            print(i[0])
            create_table_query = f"""CREATE TABLE {i[0]} (q VARCHAR(1000) NOT NULL,a VARCHAR(1000) NOT NULL)"""
            try:
                # Establish connection to the MySQL database
                cursor = conn.cursor()

                # Check if the table exists
                cursor.execute(f"SHOW TABLES LIKE '{i[0]}'")
                result = cursor.fetchone()

                if result:
                    print(f"Table '{i[0]}' already exists.")
                else:
                    # Create the table
                    cursor.execute(create_table_query)
                    print(f"Table '{i[0]}' created successfully.")

            except s.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)

            pass
            
            
    def add_question(self):
        for i in self.categories:
            n = int(input(f'Enter no. of qs for {i[0]}: '))
            for j in range(n):
                i[1].append(input('Enter q: '))
                i[2].append(input("Enter a: "))

     
        
if __name__  == '__main__':
    quiz = Quiz()
    create_sql_db()
    quiz.category()
    quiz.create_tables()
    print(quiz.categories)

