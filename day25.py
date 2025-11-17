questions = ("question 1", "question 2", "question 3")
options = (("ABCD"), ("ABCD"), ("ABCD"))
answer = "ABC"
score = 0
question_num = 0
guesses = []
for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your question:").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
    question_num += 1
