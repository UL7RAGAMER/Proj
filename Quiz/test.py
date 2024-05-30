import mysql.connector as s
from mysql.connector import errorcode
import tkinter as tk
from tkinter import messagebox, simpledialog
import asyncio
database_name = 'quiz'

conn = s.connect(host="localhost", user='root', passwd="2721")
cursor = conn.cursor()
b = False
if b:
    c = conn.cursor()   
    c.execute('drop database quiz')


def create_sql_db():
    

    # Check if database exists
    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    result = cursor.fetchone()
    cursor.execute(f"use quiz")
    if result:
        print(f"Database '{database_name}' already exists.")
    else:
        # Create the database
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database '{database_name}' created successfully.")
        cursor.execute(f"use quiz")


class Quiz:

    def __init__(self):
        self.admin_u = "1"
        self.admin_p = "2"
        self.user_u = '3'
        self.user_p = None
        self.categories = []
        

    def category(self):
        cat = int(input("Enter the number of categories: "))
        for i in range(cat):
            n = input(f'Enter the name of the category {i + 1}: ')
            q = []
            a = []
            qa = (n, q, a)
            self.categories.append(qa)
        pass

    def create_tables(self):
        conn = s.connect(host="localhost", user='root', passwd="2721", database=database_name)
        
        for i in self.categories:
            create_table_query = f"""CREATE TABLE {i[0]} (q VARCHAR(1000), a VARCHAR(1000))"""
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
        conn = s.connect(host="localhost", user='root', passwd="2721", database=database_name)
        c = conn.cursor()
        for i in self.categories:
            q = i[1]
            a = i[2]
            data = []

            for j in range(len(q)):
                x = (q[j], a[j])
                data.append(x)

            query = f"INSERT INTO {i[0]} VALUES (%s, %s)"
            c.executemany(query, data)
            conn.commit()

    def add_question(self, category_name, question, answer):
        for i in self.categories:
            if i[0] == category_name:
                i[1].append(question)
                i[2].append(answer)
                break
        else:
            messagebox.showerror("Error", f"Category '{category_name}' not found.")


class QuizGUI:
    def __init__(self, root, quiz):
        self.root = root
        self.quiz = quiz

        self.root.title("Quiz Admin")
        self.root.geometry("500x400")
        self.current_cat = ''
        self.create_login_mode_screen()
    def create_login_mode_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Do you want to login as admin/player: ",font=("Helvetica", 16),bg='#803D3B',fg='#AF8260').pack(pady=20)
        tk.Button(self.root, text="Admin",command=self.create_login_screen_admin,bg='#803D3B',fg='#AF8260').pack(pady=5)
        tk.Button(self.root, text="Player",command=self.create_login_screen_user,bg='#803D3B',fg='#AF8260').pack(pady=10)
    

    def create_login_screen_admin(self):
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Helvetica", 16),bg='#803D3B').pack(pady=20)
        
        tk.Label(self.root, text="Username",bg='#803D3B').pack()
        self.admin_user_entry = tk.Entry(self.root)
        self.admin_user_entry.pack()

        tk.Label(self.root, text="Password",bg='#803D3B').pack()
        self.admin_pass_entry = tk.Entry(self.root, show="*")
        self.admin_pass_entry.pack()

        tk.Button(self.root, text="Login", command=self.login,bg='#803D3B').pack(pady=20)
    def create_login_screen_user(self):
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Helvetica", 16),bg='#803D3B').pack(pady=20)
        
        tk.Label(self.root, text="Username",bg='#803D3B').pack()
        self.admin_user_entry = tk.Entry(self.root)
        self.admin_user_entry.pack()

        tk.Button(self.root, text="Login", command=self.test,bg='#803D3B').pack(pady=20)
    

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def test(self):
        username = self.admin_user_entry.get()
        if username:
            messagebox.showinfo("Login Success", f"Welcome {username}!")
            self.create_main_screen_u()
            
    def create_main_screen_u(self):
        self.clear_screen()
        tk.Label(self.root,text="ARE YOU SMARTER THAN A 5th GRADER",font=("Helvetica",20,"bold"),bg='#803D3B').pack(pady=50)
        tk.Button(self.root, text='START QUIZ', font=("Helvetica",20,"bold"),command=self.start_quiz,bg='#9AE474').place(relx=0.5,rely=0.5,anchor='center')

        
    def start_quiz(self):
        self.clear_screen()
        try:
            cursor.execute('SHOW TABLES')
            conn.commit()
        except s.Error as err:
            print(err)
            pass
        c = cursor.fetchall()
        a = 0
        for i in c:
            i = i[0]
            # Create buttons with unique identifiers (category) as command arguments
            button = tk.Button(self.root, text=i, command=lambda category=i: asyncio.run(self.cat_display(category)), bg='#803D3B', font=("Helvetica", 20, "bold"))
            button.place(relx=0.5, rely=0.5, anchor='center', y=a)
            a += 100  # Adjust spacing between buttons
    async def wait_until(condition):
        while not condition():
            await asyncio.sleep(1) 
            
    async def cat_display(self, category):
        def check(ans):
            return simpledialog.askstring("Category", "Enter the name of the category:") == ans
        
        cursor.execute(f'select * from {category}')
        c = cursor.fetchall()
        self.clear_screen()
        for i in c:
            print(i)
            tk.Label(self.root, text=i[0],font=("Helvetica",20,"bold"),bg='#803D3B').pack(pady=50)
            real_ans = i[1]
            await self.wait_until(lambda real_ans: check(real_ans))
        
        

    def login(self):
        username = self.admin_user_entry.get()
        password = self.admin_pass_entry.get()

        if username == self.quiz.admin_u and password == self.quiz.admin_p:
            messagebox.showinfo("Login Success", "Welcome admin!")
            self.create_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            
            
  
        
    def create_main_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Admin Panel", font=("Helvetica", 16),bg='#803D3B').pack(pady=20)

        tk.Button(self.root, text="Add Category", command=self.add_category,bg='#803D3B').pack(pady=5)
        tk.Button(self.root, text="Add Question", command=self.add_question,bg='#803D3B').pack(pady=5)
        tk.Button(self.root, text="Create Tables", command=self.quiz.create_tables,bg='#803D3B').pack(pady=5)
        tk.Button(self.root, text="Save Questions to DB", command=self.quiz.add_qa_sql,bg='#803D3B').pack(pady=5)
        tk.Button(self.root, text="Quit", command=self.create_login_mode_screen ,bg='#803D3B').pack(pady=5)

    def add_category(self):
        category_name = simpledialog.askstring("Category", "Enter the name of the category:")
        if category_name:
            self.quiz.categories.append((category_name, [], []))
            messagebox.showinfo("Success", f"Category '{category_name}' added.")

    def add_question(self):
        if not self.quiz.categories:
            messagebox.showerror("Error", "No categories found. Please add a category first.")
            return
        
        category_name = simpledialog.askstring("Category", "Enter the name of the category:")
        if category_name:
            question = simpledialog.askstring("Question", "Enter the question:")
            answer = simpledialog.askstring("Answer", "Enter the answer:")
            if question and answer:
                self.quiz.add_question(category_name, question, answer)
                messagebox.showinfo("Success", "Question and answer added.")

if __name__ == "__main__":
    create_sql_db()
    quiz = Quiz()

    root = tk.Tk()
    root.configure(bg='#322C2B')
    gui = QuizGUI(root, quiz)
    root.mainloop()
