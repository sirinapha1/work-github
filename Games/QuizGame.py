print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' 1+2=? \n ')
if answer.lower() == '3':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' 5+6=? \n ')
if answer.lower() == '11':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' 1+1=? \n ')
if answer.lower() == '2':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('30+25? \n ')
if answer.lower() == '55':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' 60+30=? \n ')
if answer.lower() == '90':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")
