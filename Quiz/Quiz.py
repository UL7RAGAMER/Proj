import mysql.connector as s
def login_sql():
    mycon=s.connect(host="localhost",user='root',passwd="272",database='quiz')
    
class Quiz:
    def __init__ (self):
        self.admin_u="1"
        self.admin_p="2"
        self.categories = [] ; list
         
    def login(self):
        access = False
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
        cat=int(input("Enter the no of categories: "))
        for i in range(cat):
            n = input(f'Enter name of the category {i+1}:  ')
            q = []
            a = []
            qa = (n,q,a)
            self.categories.append(qa)  
        pass
    def add_question(self):
        for i in self.categories:
            n = int(input(f'Enter no. of qs for {i[0]}: '))
            for j in range(n):
                i[1].append(input('Enter q: '))
                i[2].append(input("Enter a: "))

    def start(self):
        pass
        
        
if __name__  == '__main__':
    quiz = Quiz()
    quiz.login()
    quiz.category()
    quiz.add_question()
    print(quiz.categories)
    pass
