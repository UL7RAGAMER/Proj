class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        
    def add_question(self, question, answer):
        self.questions.append({"question": question, "answer": answer})

    def take_quiz(self):
        for q in self.questions:
            print(q["question"])
            user_answer = input("Your answer: ")
            if user_answer.lower() == q["answer"].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect! The correct answer was:", q["answer"])
        print(f"Your final score is {self.score}/{len(self.questions)}")

def create_quiz():
    quiz = Quiz()
    
    # Add your questions here
    n= int(input('Enter no. of questions: '))
    for i in range(n):
        quiz.add_question(input('Enter your question: '), input('Enter your anwser: '))

    
    return quiz

if __name__ == "__main__":
    quiz = create_quiz()
    quiz.take_quiz()
