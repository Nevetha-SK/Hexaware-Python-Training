# Python quiz questions and answers
quiz = {
    "Which keyword is used to define a function in Python?": (
        ("A. func", "B. def", "C. function", "D. define"), "B"),
    
    "Which data type is immutable in Python?": (
        ("A. List", "B. Set", "C. Dictionary", "D. Tuple"), "D"),
    
    "What does the len() function do?": (
        ("A. Adds numbers", "B. Returns length", "C. Sorts list", "D. Converts to string"), "B"),
    
    "Which symbol is used to comment a single line in Python?": (
        ("A. //", "B. <!--", "C. #", "D. **"), "C"),
    
    "Which loop is used to iterate a known number of times?": (
        ("A. for", "B. while", "C. do-while", "D. switch"), "A")
}

# Lambda to assign grade
grade = lambda score, total: "A" if score == total else "B" if score >= total * 0.6 else "F"

# Function to start the quiz
def start_quiz():
    name = input("Enter your name: ")
    score = 0

    for q, (opts, correct) in quiz.items():
        print("\n" + q)
        for opt in opts:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").upper()
        if ans == correct:
            print("✅ Correct")
            score += 1
        else:
            print(f"❌ Wrong (Correct: {correct})")

    total = len(quiz)
    print(f"\n{name}, your score is {score}/{total}")
    print("Grade:", grade(score, total))

# Run the quiz
start_quiz()
