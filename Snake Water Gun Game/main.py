import random as r

options = ("snake", "water", "gun")

def game():
    user = input("Enter your choice: ").lower()
    comp = r.choice(options)
    print(f"Computer's choice: {comp}")

    if user == comp:
        print("It's a tie!")
    elif user == "snake":
        if comp == "water":
            print("You win!")
        else:
            print("Computer wins!")
    elif user == "water":
        if comp == "gun":
            print("You win!")
        else:
            print("Computer wins!")
    elif user == "gun":
        if comp == "snake":
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid input! Try again.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        game()
    else:
        print("Thanks for playing!")

game()

