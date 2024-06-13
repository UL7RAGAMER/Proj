import mysql.connector as s
from mysql.connector import errorcode
import tkinter as tk
from tkinter import messagebox
database_name = 'quiz'

conn=s.connect(host="localhost",user='root',passwd="2721")
b=False
if b:
    c = conn.cursor()
    c.execute('drop database quiz')


def create_sql_db():
    
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
            create_table_query = f"""CREATE TABLE {i[0]} (q VARCHAR(1000),a VARCHAR(1000))"""
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

    
    def add_qa_sql(self):
        conn=s.connect(host="localhost",user='root',passwd="2721",database = database_name)
        c = conn.cursor()
        c.execute('Show tables')
        d=c.fetchall()
        for i in self.categories:
            q = i[1]
            a = i[2]
            data =  []
            
            for j in range(len(q)):
                x = (q[j],a[j])
                data.append(x)
                
            query = f"INSERT INTO {i[0]} VALUES (%s, %s)"
            c.executemany(query, data)
            conn.commit()

    def add_question(self):
        for i in self.categories:
            n = int(input(f'Enter no. of qs for {i[0]}: '))
            for j in range(n):
                i[1].append(input('Enter q: '))
                i[2].append(input("Enter a: "))

     
class Gui:
    
    def __init__(self) -> None:
        pass
    
    def create_ui(self):
    # Create the main window
        root = tk.Tk()
        root.title("Place Example with Separation for Labels")

        # Define the separation between labels
        separation_y = 80
        start_x = 10
        start_y = 20
        
        # Create labels
        labels_text = ['1) ADD QUESTIONS', '2) DELETE QUESTIONS', '3) ADD ANSWERS', '4) MODIFY QUESTIONS']
        labels = [tk.Label(root, text=text, font=("Times New Roman 24", 20,'bold')) for text in labels_text]

        # Place labels with calculated positions
        for i, label in enumerate(labels):
            label.place(x=start_x, y=start_y + i * separation_y)
        separation_y = 80
        start_x =400
        start_y = 10
        def add_questions():
             messagebox.showinfo("Add Questions button clicked", "Functionality to add questions will be implemented.")

        def delete_questions():
             messagebox.showinfo("Delete Questions button clicked", "Functionality to add questions will be implemented.")

        def add_answers():
             messagebox.showinfo("Add Answers button clicked", "Functionality to add questions will be implemented.")

        def modify_questions():
             messagebox.showinfo("Modify Questions button clicked", "Functionality to add questions will be implemented.")
        # Create labels
        buttons_text = [
        ('1) ADD QUESTIONS', add_questions),
        ('2) DELETE QUESTIONS', delete_questions),
        ('3) ADD ANSWERS', add_answers),
        ('4) MODIFY QUESTIONS', modify_questions)]
        buttons = [tk.Button(root, text=text,command=command , font=("Times New Roman 24", 20,'bold')) for text, command in buttons_text]

        # Place labels with calculated positions
        for i, button in enumerate(buttons):
            button.place(x=start_x, y=start_y + i * separation_y)    
        root.mainloop()

 
if __name__  == '__main__':
    gui=Gui()
    gui.create_ui()
'''   quiz = Quiz()
    create_sql_db()
    quiz.category()
    quiz.create_tables()
    quiz.add_question()
    quiz.add_qa_sql()'''

