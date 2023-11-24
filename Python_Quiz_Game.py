#Quiz game
print("**************************")
print("Welcome to My Quiz Game!!!")  

question_bank = [
    {"text":"Who developed the Python language?","answer":"B"},
    {"text":"What is the maximum length of a Python identifier?","answer":"D"},
    {"text":"The ability of one class to acuire methods and attributes of another class is called ________.","answer":"A"},
    {"text":"In which year was the Python language developed?","answer":"D"},
    {"text":"Which of the following is a type of inheritance?","answer":"D"},
    {"text":" What is the method inside the class in python language?","answer":"B"},
    {"text":"What type of inheritance has multiple subclass to a single super class?","answer":"C"},
    {"text":"What is the depth of multilevel inheritance in python?","answer":"C"},
    {"text":"What does MRO stand for?","answer":"B"},
    {"text":"Which of the following precedence order is correct in Python?","answer":"A"}
]

options = [
          ["A. Zim Den","B. Guido van Rossum","C. Niene Stom","D. Wick van Rossum"],
          ["A. 32","B. 16","C. 128","D. No fixed length is specified"],
          ["A. Inheritance","B. Abstraction","C. Polymorphism","D. Object"],
          ["A. 1995","B. 1972","C. 1981","D. 1989"],
          ["A. Single","B. Double","C. Multiple","D.both A and C"],
          ["A. Object","B. Function","C. Attribute","D. Argument"],
          ["A. Multiple Inheritance","B. Multilevel Inheritance","C. Hierarchical Inheritance","D. None of the above"],
          ["A. Two level","B. Three level","C. Any level","D. None of these"],
          ["A. Method Recursive Object","B. Method Resolution Order","C. Main Resolution Order","D. Method Rational Order"],
          ["A. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction","B. Multiplication, Division, Addition, Subtraction, Parentheses, Exponential","C. Division, Multiplication, Addition, Subtraction, Parentheses, Exponential","D. Exponential, Parentheses, Multiplication, Division, Addition, Subtraction"]
          ]
score = 0

def check_answer(user_guess,correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False


for question_num in range(len(question_bank)):
    print("\n**************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
        
    guess = input("\nEnter your answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess,question_bank[question_num]["answer"])
    
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect!!!!")
        print("The correct answer is :",question_bank[question_num]["answer"])
    print(f"Your corrent score is :{score}/{(question_num+1)}")     
        
print("\nNumber of correct answers:",score)
print(f"Your score is {(score/len(question_bank))*100}%")