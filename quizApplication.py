import random

def quiz_game():
    
    questions = {
        "What is the capital of France?": (["Paris", "London", "Berlin", "Madrid"], "Paris"),
        "What is the largest planet in our solar system?": (["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"),
        "Who painted the Mona Lisa?": (["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "Leonardo da Vinci"),
        "What is the chemical symbol for gold?": (["Ag", "Au", "Fe", "Cu"], "Au"),
        "In which year did World War II end?": (["1945", "1949", "1939", "1941"], "1945")
    }

    question_list = list(questions.keys())
    random.shuffle(question_list)

    score = 0
    for question in question_list:
        options, correct_answer = questions[question]
        print(f"\nQuestion: {question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = input("Enter your answer (1-4): ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                if options[user_answer - 1] == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is: {correct_answer}")
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYour score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
    