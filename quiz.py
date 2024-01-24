import random

class QuestionGame:
    def __init__(self):
        self.score = 0
        self.used_questions = [] #don't repeat questions
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
            {"question": "What is the largest desert in the world?", "answer": "Antarctica"},
            {"question": "Who is the author of 'Harry Potter' series?", "answer": "J.K. Rowling"},
            {"question": "What is the currency of Japan?", "answer": "Yen"},
            {"question": "Which planet is known as the 'Blue Planet'?", "answer": "Earth"},
            {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
            {"question": "What is the capital of Australia?", "answer": "Canberra"},
            {"question": "Which country is famous for the pyramids?", "answer": "Egypt"},
            {"question": "What is the smallest prime number?", "answer": "2"},
        ]

    def ask_question(self):
        available_questions = [q for q in self.questions if q not in self.used_questions]

        if not available_questions:
            print("There are no more questions available.")
            return

        question = random.choice(available_questions)
        self.used_questions.append(question)

        user_answer = input(question["question"] + "\nYour answer: ")

        if user_answer.lower() == question["answer"].lower():
            print("Correct! You earned +10 points.")
            self.score += 10
        else:
            print(f"Sorry, wrong answer. The correct answer is: {question['answer']}")

    def start_game(self):
        print("Welcome to the Question Game!")
        while True:
            self.ask_question()
            continue_game = input("Do you want another question? (Yes/No): ")
            if continue_game.lower() != "yes":
                print(f"The game has ended. Your total score is: {self.score}")
                break

if __name__ == "__main__":
    game = QuestionGame()
    game.start_game()
