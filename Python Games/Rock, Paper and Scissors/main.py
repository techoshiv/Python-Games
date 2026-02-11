import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

games_images= [rock,paper,scissors]
player_chose=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
print(games_images[player_chose])
computer_chose=random.randint(0,2)
print("Computer chose"+games_images[computer_chose])

if player_chose==computer_chose:
     print("It's a draw!")
elif player_chose==0 and computer_chose==1:
    print("You lose!")
elif player_chose== 0 and computer_chose== 2:
    print("You win!")
elif player_chose==1 and computer_chose==0:
    print("You win!")
elif player_chose==1 and computer_chose==2:
    print("You win!")
elif player_chose==2 and computer_chose==0:
    print("You lose!")
elif player_chose==2 and computer_chose==1:
    print("You win!")
else:
    print("Enter a valid choice!")


