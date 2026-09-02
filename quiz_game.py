print("Welcome to the Quiz Game!")
questions = { 
    'What is the capital of France?': {'choices': ['A) Spain', 'B) Paris', 'C) Brazil', 'D) Argentina'], 'answer': 'B'},
    'What is the largest planet in our solar system?': {'choices': ['A) Saturn', 'B) Uranus', 'C) Mercury', 'D) Jupiter'], 'answer': 'D'},
    'What is the chemical symbol for gold?': {'choices': ['A) Au', 'B) Bc', 'C) Pb', 'D) Fe'], 'answer': 'A'},
    'Who wrote the play "Romeo and Juliet"?': {'choices': ['A) Charles Dickens', 'B) William Shakespeare', 'C) Jane Austen', 'D) Mark Twain'], 'answer': 'B'},    
    'What is the smallest prime number?': {'choices': ['A) 0', 'B) 1', 'C) 9', 'D) 2'], 'answer': 'D'},
    'What is the square root of 64?': {'choices': ['A) 6', 'B) 7', 'C) 8', 'D) 9'], 'answer': 'C'}
}
def ask_question(question, answer):
    print(question)
    choices = answer['choices']
    correct_letter = answer['answer']
    for choice in choices:
        print(choice)
    player_answer = input("Enter your answer (A/B/C/D): ").lower()
    if player_answer.upper() == correct_letter.upper():
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer is {correct_letter}.")
        return False
play_again = "Yes"
score = 0
while play_again.lower() == "yes":
    score = 0
    for question, answer in questions.items():
        is_currect = ask_question(question, answer)
        if is_currect:
            score += 1
    print(f"You scored {score} out of {len(questions)}.")
    with open("scores.txt", "a") as file:
        file.write(f"Score: {score}/{len(questions)}\n")
    if score == len(questions):
        print("Congratulations! You got a perfect score!")
    elif score >= len(questions) / 2:
        print("Good job! You know your stuff.")
    else:
        print("Keep practicing! You'll get better with more practice.")
    play_again = input("Do you want to play again? (Yes/No): ")