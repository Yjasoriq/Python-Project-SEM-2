import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)

    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


def tic_tac_toe():
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 10)

    def check_winner(board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, 2) for your move: "))
        col = int(input("Enter column (0, 1, 2) for your move: "))
        if board[row][col] != " ":
            print("That position is already occupied! Try again.")
            continue
        board[row][col] = players[current_player]
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break
        current_player = (current_player + 1) % 2

def hangman2():

 def choose_word():
     words = ["python", "hangman", "computer", "programming", "gaming", "code"]
     return random.choice(words)

 def display_word(word, guessed_letters):
     display = ""
     for letter in word:
         if letter in guessed_letters:
             display += letter
         else:
             display += "_"
     return display

 def hangman():
     word = choose_word()
     guessed_letters = []
     attempts = 10
     print("Welcome to Hangman!")
     print("Try to guess the word. You have 10 attempts.")

     while attempts > 0:
         print("\n" + display_word(word, guessed_letters))

         guess = input("Guess a letter: ").lower()

         if len(guess) != 1 or not guess.isalpha():
             print("Please enter a single letter.")
             continue

         if guess in guessed_letters:
             print("You already guessed that letter.")
             continue

         guessed_letters.append(guess)

         if guess not in word:
             attempts -= 1
             print("Wrong guess! You have {} attempts left.".format(attempts))
             if attempts == 0:
                 print("You're out of attempts! The word was '{}'.".format(word))
                 break
         else:
             if "_" not in display_word(word, guessed_letters):
                 print("Congratulations! You've guessed the word: '{}'".format(word))
                 break

     play_again = input("Do you want to play again? (yes/no): ").lower()
     if play_again == "yes":
         hangman()
     else:
         print("Thanks for playing!")

 hangman()

def fourinarow():
 def print_board(board):
     for row in board:
         print(" | ".join(row))
         print("-" * (7 * len(row) - 1))

 def check_winner(board, player):
     # Check horizontally
     for row in board:
         for i in range(len(row) - 3):
             if all(cell == player for cell in row[i:i+4]):
                 return True

    # Check vertically
     for col in range(len(board[0])):
         for i in range(len(board) - 3):
             if all(board[i+j][col] == player for j in range(4)):
                 return True

    # Check diagonally (top-left to bottom-right)
     for i in range(len(board) - 3):
         for j in range(len(board[0]) - 3):
             if all(board[i+k][j+k] == player for k in range(4)):
                 return True

    # Check diagonally (top-right to bottom-left)
     for i in range(len(board) - 3):
         for j in range(3, len(board[0])):
             if all(board[i+k][j-k] == player for k in range(4)):
                 return True

     return False

 def is_board_full(board):
     return all(cell != ' ' for row in board for cell in row)

 def connect_four():
     rows = 6
     cols = 7
     board = [[' ' for _ in range(cols)] for _ in range(rows)]
     current_player = 'X'

     while True:
         print_board(board)
         col = int(input(f"Player {current_player}, enter the column (0-{cols-1}): "))

         for row in range(rows - 1, -1, -1):
             if board[row][col] == ' ':
                 board[row][col] = current_player

                 if check_winner(board, current_player):
                     print_board(board)
                     print(f"Player {current_player} wins!")
                     return
                 elif is_board_full(board):
                     print_board(board)
                     print("It's a tie!")
                     return

                 current_player = 'O' if current_player == 'X' else 'X'
                 break
         else:
             print("Column is full. Choose another column.")

 connect_four()

def nameguess():
 def name_guessing_game(names):
     target_name = random.choice(names)
     attempts = 0
     guessed_name = ""

     print("Welcome to the Name Guessing Game!")
     print("I have chosen a name. Try to guess it.")

     while guessed_name.lower() != target_name.lower():
         guessed_name = input("Enter your guess: ")
         attempts += 1

         if guessed_name.lower() == target_name.lower():
             print("Congratulations! You guessed the name '{}' in {} attempts.".format(target_name, attempts))
         else:
             print("Sorry, that's not the correct name. Try again.")

 def name():
     names = ["KRISH", "ASHUTOSH", "VANSH", "PANKAJ", "SARITA", "SARITA", "GANESH", "KISHORI", "SHALU", "GAURI"]
     name_guessing_game(names)

 name()

def display_menu():
    print("PYTHON PROJECT BY YASH JASORIA")
    print("Menu:")
    print("1. Number Guessing Game")
    print("2. Tic Tac Toe")
    print("3. Four in a row")
    print("4. Hangman")
    print("5. Name guessing game")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            tic_tac_toe()
        elif choice == '3':
            fourinarow()
        elif choice == '4':
           hangman2()
        elif choice == '5':
           print("The names will be KRISH, ASHUTOSH, VANSH, PANKAJ, SARITA, GANESH, KISHORI, SHALU, GAURI, ANJU")
           nameguess()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 3.")

main()
