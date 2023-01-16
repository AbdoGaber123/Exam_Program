""""
created on Tue Jan 17 6:30:00 2023
@author:AbdallahGaber 
"""
"""
Now we are goning to create an Exam program that consists of many
qouestions . The Process is we ask a question , then , the user give
an answer, we say is it correct or not , we also collect the correct 
answers and store them into variable, finllay we tell the user his 
score and percentage.
# in this program we use dictionary data type to store qouestions and answers 
"""
# At first we create a list of the Questions and answers
Exam = {
    "Qouestion 1":{
    "Qouestion": "Where was prophet Mohamed born?",
    "Answer"    : "Makkah"
    },
    "Qouestion 2":{
    "Qouestion": "How old was prophet Mohamed when he died ?",
    "Answer"    : "63"
    },
    "Qouestion 3": {
        "Qouestion": "Where was prophet Mohamed buried?",
        "Answer"    : "Maddinah"
    },
    "Qouestion 4": {
        "Qouestion": "Where is the capital of Egypt?",
        "Answer"    : "Cairo"
    },
    "Qouestion 5": {
        "Qouestion": "What is the captial of Saudi Arabia?",
        "Answer"    : "Rayaid"
    },
    "Qouestion 6": {
        "Qouestion": "When was the web introduced for the first time?",
        "Answer"    : "1991"
    },
    "Qouestion 7": {
        "Qouestion": "What is the captial of Palstine?",
        "Answer"    : "Kods"
    },
    "Qouestion 8": {
        "Qouestion": "What is the captial of Iraq?",
        "Answer"    : "Beghdad"
    },
    "Qouestion 9": {
        "Qouestion": "What is the captial of Qatar?",
        "Answer"    : "Doha"
    },
    "Qouestion 10": {
        "Qouestion": "What is the captial of Sayria?",
        "Answer"    : "Dimashaq"
    }
}

#initialze counter to store the score
total_score = 0
i = 0
#make a loop in all question and answers
for key , value in Exam.items():
    i += 1
    print("Question number",str(i))
    print(value['Qouestion'])                                   # printing the Question
    the_answer = input("Enter Your Answer: ")
    if the_answer.lower() == value['Answer'].lower():           # checking the user answer
        print('Correct Answer')
        total_score += 1                                        # increasing the score of correct answers
        print('Your score now is : ', str(total_score))
        print("")
    else:
        print('Wrong Answer')
        print('The correct answer is: ', value['Answer'])       
        print("")

print("Your Final Result is: " , str(total_score) , "out of 10")
print("Your Final Result is: " , str((total_score / 10) * 100 ))












