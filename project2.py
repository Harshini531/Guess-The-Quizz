print("Welcome to my computer quizz!")
playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Lets's play:)")
score = 0

answer = input("What does GOOGLE stands for?")
if answer =="Global Organization of Oriented Group Language of Earth":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does YAHOO stands for?")
if answer =="Yet Another Hierarchical Officious Oracle":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does Wi-Fi stands for?")
if answer =="Wireless Fidelity":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PAN stands for?")
if answer =="Permanent Account Number":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does  PDF stands for?")
if answer =="Portable Document Format":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("you got + str(score) + question correct! ")
print("you got" + str((score/4)*100) +"%.")
