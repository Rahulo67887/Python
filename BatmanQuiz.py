questions=("Whose the newest batman?",
            "Who directed the latest batman film?",
            "The latest batman film is related to which studio?",
            "Is the latest batman film related to DCEU?",
            "Does the fans liked the latest batman film?")

options=(("A.Chritian Bale", "B.Robert Pattinson", "C.Ben Affleck", "D.Salman Khan"),
         ("A.Matt Reves", "B.Christopher Nolan", "C.Zack Snyder", "D.James Gunn"),
         ("A.Marvel", "B.DC", "C.Universal", "D.T-series"),
         ("A.Yes", "B.No", "C.Not totally", "D.Not Decided"),
         ("A.Yes", "B.No", "C.Not Totally", "D.Some Fans"))

answers=("B", "A", "B", "B", "A")
ques_num=0
guesses=[]
score=0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)
    guess=input("Enter your answer:").upper()
    guesses.append(guess)
    if(guess==answers[ques_num]):
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        print(f"Correct answer is {answers[ques_num]}")
    ques_num+=1

print()   
print("           RESULT            ")
print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print() 

print("Your Guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print() 

score=score/len(questions)*100
print(f"Your Score is:{score}")
        