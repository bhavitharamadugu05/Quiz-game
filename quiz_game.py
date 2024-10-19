def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["a) Paris", "b) London", "c) Rome"],
            "answer": "a"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["a) Mars", "b) Venus", "c) Jupiter"],
            "answer": "a"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": ["a) Leonardo da Vinci", "b) Pablo Picasso", "c) Vincent van Gogh"],
            "answer": "a"
        }
    ]

    score = 0  

    print("Multiple-Choice Quiz Game\n")

    for idx, question in enumerate(questions):
        print(f"{idx + 1}. {question['question']}")
        for choice in question['choices']:
            print(choice)

        user_answer = input("\n> ").lower()  

        if user_answer == question['answer']:
            print("Correct!\n")
            score += 1  
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.\n")

    print("Quiz complete!")
    print(f"You answered {score} out of {len(questions)} questions correctly.")

if __name__ == "__main__":
    quiz_game()
