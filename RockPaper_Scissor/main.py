import random

#Rock Paper Scissors Game


running = True
while running:
    
    print("Let's Play Rock Paper Scissor Game!!!")

    print(end=None)


    user = input("Enter a Choice (rock, paper, scissors): ")
    user = user.title()
    computer_choice = ['rock', 'paper', 'scissors']

    computer = random.choice(computer_choice)
    computer = computer.title()
    print(f"\nYou chose {user}, computer chose {computer}.\n")


    user = user.lower()
    computer = computer.lower()


    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    playing = input("Do you want to play again? (Y, N) ")
    playing = playing.upper()
    if playing == 'Y':
        running = True
    else:
        running = False
