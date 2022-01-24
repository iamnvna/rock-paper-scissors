import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter either Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == 'q':
        print("Goodbye!")
        break

    if user_input not in options:
        print("Enter a valid input!")
        continue

    random_number = random.randint(0, 2)
    computer_input = options[random_number]

    if user_input == "rock" and computer_input == "scissors":
        print("You won!")
        user_score += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You won!")
        user_score += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You won!")
        user_score +=1
    else:
        print("You lost!")
        computer_score += 1


if user_score < computer_score:
    print("\nWinner: Computer!")
elif user_score == computer_score:
    print("You drew!")
else:
    print("Winner: You! :)")
print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")

# Commentary
"""
Line 1:
    The random variable is imported to allow the program make a random
    guess between rock, paper, and scissors using lists.

Line 3-4:
    These lines create variables to hold the user score and the computer 
    score. When compared in line 34, we get a winner.

Line 5: 
    The option variable holds a list of strings that are the options
    available in the rock, paper, scissors game. The list is used in the 
    code below.

Line 7:
    The while True conditional statement allows the code to restart from
    that point or break out entirely from the loop using the 'break' and 
    'continue' keywords.

Line 8:
    Line 8 collects the user input or option from the user to compare with 
    the computer chosen option to determine if the user on or not. An optional
    input Q is collected from the user to quit the program where they do not
    want to continue playing. The .lower() method appended to the input
    statement converts the user input into lowercase letters. 
    
Line 9-11:
    This block of code evaluates the user input to determine if the user entered
    'Q'. The program shuts if it evaluates to true. 
    
Line 13-15:
    This block of code evaluates the user input to determine if it matches any
    of the options defined in the 'options' variable. Where is doesn't, the user
    is prompted to enter a valid input. 
    
Line 17:
    This line of code uses a the randint() method to assign a random integer from
    0 to 2 to the random_number variable.

Line 18: 
    The computer input is then assigned a value from the options (list) using the
    index of the option. The index is the random number chosen by the program from
    line 17.
    
Line 20-31:
    This block of code is based of the rules in the rock, paper, scissors game. 
    Using the if conditional statement, options from the computer are evaluated
    against options from the user. Where the inputs show a correct user prediction,
    "You won!" is printed out to the console. Otherwise, "You lost!" is printed
    to the console. Where the user wins, one is added to the user_score variable. 
    Likewise for the computer wins (user loses).

Line 34-41:
    This block of code runs when the user quits the program after playing for a while.
    The user_score is compared to the computer_score and a winner selected using if
    conditional statements. The user_score is printed on the screen, and the 
    computer_score is printed on the screen to this effect.
"""