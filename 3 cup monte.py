import random

#A list named 'cups' is created with three elements: "a", "b", and "c". 
# Each represents a possible cup under which a hidden object might be placed.

cups = ["a","b","c"] 
#The program prints a welcome message to the player,
#  explaining that they need to guess which cup (among "a", "b", or "c") has the hidden object.

print("Welcome to the 3-Cup Monte game!")
print("Try to find the hidden cup among a, b, and c.")



while True: #A while loop begins, which will continue to run the game until the player decides to stop
#Inside the loop, the program uses the 'random.choice()' function to randomly select one cup from the 'cups' list. 
# This 'cup' is stored in the 'hidden_cup' variable, representing where the hidden object is placed for this round.
    hidden_cup = random.choice(cups)
#The player is prompted to input their choice of cup by typing "a", "b", or "c".
#  The choice is stored in the 'choice' variable.
    choice = input("Which cup do you choose? (a, b, or c): ")

#The program compares the player's choice (choice) with the randomly selected hidden cup (hidden_cup):
    if choice == hidden_cup: 
        print("Good Job!!")
    else:
        print("try again:")
#After each round, the program asks the player if they want to play again by typing "yes" or "no".
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break
    print("Thank you for playing 3 Cup Monte game!")