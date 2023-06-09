print("Welcome future baller")

playing= input("Do you think you are a baller? ")

if playing.lower() != "yes":
    quit()

score = 0

print("Kick of begins now")


answer = input("How many football players are on the pitch? ")
if answer.lower() == "22":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT")   

answer = input("What is the name of the player who guards the goal? ")
if answer.lower() == "goalkeeper":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 

answer = input("How many teams play in the Premier League? ")
if answer.lower() == "20":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 

answer = input("Who is the current England manager? ")
if answer.lower() == "gareth southgate":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 

answer = input("What country does Messi play for? ")
if answer.lower() == "argentina":
    print("Goal!!!")
    score +=1
else:
    print("Missed try again") 

answer = input("What colours does Manchester united play in? ")
if answer.lower() == "red":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 
answer = input("How long is one half of a game? ")
if answer.lower() == "45 minuets":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 

answer = input("What country is David Beckham from? ")
if answer.lower() == "england":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 

answer = input("Which country has won the most world cups? ")
if answer.lower() == "brazil":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 

answer = input("Who is the Goat ")
if answer.lower() == "cristiano ronaldo":
    print("Goal!!!")
    score +=1
else:
    print("INCORRECT") 
print("You scored"  + str(score) +  "questions correct")
print("You scored " + str((score/10)*100) +  "%")




  
 
