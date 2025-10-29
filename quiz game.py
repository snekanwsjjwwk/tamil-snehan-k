# Simple Quiz Game

def quiz_game():
    print("🎮 Welcome to the Quiz Game! 🎯")
    print("You will be asked 5 questions. Let's begin!\n")

    # Questions, Options, and Answers
    questions = [
        {
            "question": "1. What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "2. Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "3. What is the largest ocean on Earth?",
            "options": ["A. Indian", "B. Atlantic", "C. Arctic", "D. Pacific"],
            "answer": "D"
        },
        {
            "question": "4. Who developed the theory of relativity?",
            "options": ["A. Newton", "B. Einstein", "C. Galileo", "D. Tesla"],
            "answer": "B"
        },
        {
            "question": "5. What is the national animal of India?",
            "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Peacock"],
            "answer": "B"
        }
    ]

    score = 0

    
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print("🎉 Quiz Over! 🎉")
    print(f"Your Final Score: {score}/{len(questions)}")

    # Feedback
    if score == len(questions):
        print("🏆 Excellent! You got all answers right!")
    elif score >= 3:
        print("👍 Good job! You know quite a bit.")
    else:
        print("📚 Keep learning! You’ll do better next time.")


quiz_game()
