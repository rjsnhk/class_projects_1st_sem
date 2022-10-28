'''Project 2:
Create the Rock, Paper and Scissors game with Python,
 we need to take the user’s choice and then we need to compare
 it with the computer choice which is taken using the random module in Python
  from a list of choices, and if the user wins, then the score will increase by 1.
Example:
User: Rock, Paper or Scissors?
CPU: rock
Tie
User: Rock, Paper or Scissors?
CPU: paper
You win! Paper covers Rock
User: Rock, Paper or Scissors?
CPU: scissors
You lose… Rock smashes Scissors
Rock, Paper or Scissors?
End the game
Final Scores:
CPU:1
User:1

Hint: Make use of random module to design the game
(Student is free to decide the input and output layout for this mini project)'''
import random
Cchoice=['Rock','Paper','Scissor']
while True:
    print('Rock Paper Scissor Game:')
    youwin,youloss=0,0
    for i in range(1,6):
        print('Round',i,'Start:')
        print('Please select any one option:')
        print('1.Rock','2.Paper','3.Scissor',sep='\n')
        Yourchoice=int(input())
        if Yourchoice==1:
            print('You Select Rock')
            Yourchoice='Rock'
        elif Yourchoice==2:
            print('You Select Paper')
            Yourchoice='Paper'
        elif Yourchoice==3:
            print('You Select Scissor')
            Yourchoice='Scissor'
        else:
            print('Invailed Choice')
            break
        Computerchoice=random.choice(Cchoice)
        print('Computer Select:',Computerchoice)

        if (Yourchoice==Computerchoice):
                  youwin+=0
                  youloss+=0
                  print("Tie:")
        elif (Yourchoice=='Rock' and Computerchoice=='Scissor'):
            youwin+=1
            print('You win! Rock Smashes Scissor')
        elif (Yourchoice=='Paper' and Computerchoice=='Rock'):
            youwin+=1
            print('You win! Paper covers Rock')
        elif (Yourchoice=='Scissor' and Computerchoice=='Paper'):
            youwin+=1
            print('You win! Scissor cuts paper')
        elif(Yourchoice=='Rock' and Computerchoice=="Paper"):
            youloss+=1
            print('You loss....Paper covers Rock')
        elif(Yourchoice=='Paper' and Computerchoice=='Scissor'):
            youloss+=1
            print('You loss....Scissor cuts paper')
        elif(Yourchoice=='Scissor' and Computerchoice=='Rock'):
            youloss+=1
            print('You loss....Rock Smashes Scissor')
        else:
            print('invailed input')
        if (youwin>youloss):
            print('You Win The Game:')
            print('Score is:','Your Score:',youwin,'Computer score:',youloss,sep='')
        elif(youloss>youwin):
            print('You Loss The Game. LOL:')
            print('Score is:','Your Score:',youwin,'Computer score:',youloss,sep='')
        else:
            print('Match Drawn')
            print('Score is:', 'Your Score:', youwin, 'Computer score:', youloss, sep='')
        user_choice=input('Want to Play again ?(Yes/Exit)')
        if user_choice=='Yes' or user_choice=='yes' or user_choice=='YES' :
            continue
        else:
            break


































