import random 

while True:
    user_actions = input('Enter a choice(R - Rock, P - Paper, S - Scissors): ')
    user_actions = user_actions.upper()
    actions = ['R', 'P', 'S'] 
    

    CPU = random.choice(actions)
    if user_actions not in actions:
        print('Wrong input!, choose between R, P, S')
    else:
        print(f"\nYou choose {user_actions}, computer choose {CPU}.\n")

    if user_actions == CPU:
        print(f"Both players selected {user_actions}. It's a tie!")
    elif user_actions == "R":
        if CPU == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_actions == "P":
        if CPU == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_actions == "S":
        if CPU == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        
        
    play_again = input("Do you want to Play again? (y/n): ")
    if play_again.lower() != "y":
        print('Game over, thanks for playing!')
        break
    
