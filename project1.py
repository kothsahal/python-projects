# Quiz Application

questions = [
    {
        "question": "1. Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. display()", "D. show()"],
        "answer": "B"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. !"],
        "answer": "C"
    },
    {
        "question": "4. Which data type stores multiple values?",
        "options": ["A. int", "B. float", "C. list", "D. bool"],
        "answer": "C"
    },
    {
        "question": "5. Which loop is used to iterate over a sequence?",
        "options": ["A. for", "B. if", "C. else", "D. break"],
        "answer": "A"
    }
]

score = 0

print("===== WELCOME TO QUIZ APPLICATION =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid option!")
    elif user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

print("\n===== QUIZ RESULT =====")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("Total Questions:", total_questions)
print("Correct Answers:", score)
print("Wrong Answers:", total_questions - score)
print("Your Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent Performance!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("You can do better!")
else:
    print("Keep Practicing!")