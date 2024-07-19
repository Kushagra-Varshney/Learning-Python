import random as r

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
        self.guessed = False

    def guess(self, n):
        if self.lives > 0:
            if (n == self.number):
                self.guessed = True
                print(f"You guessed it! The number was {self.number}")
            elif(n < self.number):
                self.lives -= 1
                print(f"Wrong! You have {self.lives} lives left", "Try guessing higher")
            else:
                self.lives -= 1
                print(f"Wrong! You have {self.lives} lives left", "Try guessing lower")
        else:
            print("You have no more lives left! Game over!")

    def is_guessed(self):
        return self.guessed
    
    def get_lives(self):
        return self.lives

# Usage
guesser = Guesser(r.randint(1, 100), 10)

while (not guesser.is_guessed()):
    guess = int(input("Enter your guess: "))
    guesser.guess(guess)

    if guesser.get_lives() == 0:
        print(f"The number was {guesser.number}", "Game over! Thanks for Playing!")
        break


