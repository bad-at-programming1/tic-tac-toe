board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
turn2text = lambda t : "Player 1" if t == 1 else "Player 2"
def main():
    intro()
    while True:
        turn = 1
        for i in range(9):
            print(f"It is now {turn2text(turn)}'s turn")
            print("The board currently looks like this:")
            print_board()
            print(f"{turn2text(turn)}, it is now your turn")
            get_moves(turn)
            if result_check():
                game_over(turn)
                break
            turn = 1 if turn == 2 else 2
        else:
            print("The game is a tie. The final board looks like this:")
            print_board()
        while True:
            try:
                result = input("Would you like to play again? (y or n)").lower()
            except Exception:
                print("Invalid answer")
            if result == "y":
                break
            elif result == "n":
                print("Thank you for playing")
                exit()
            else:
                print("Invalid answer")

def game_over(r):
    print(f"{turn2text(r)} has won the game. The final board looks like this:")
    print_board()

def intro():
    print("Welcome to Tic-Tac-Toe!")
    print("Type A to begin the game")
    print("Type B to explain the rules")
    print("Type C to exit the game")
    while True:
        try:
            response = input("What would you like to do?").lower()
        except Exception:
            print("Invalid option")

        if response == "a":
            print("Beginning game")
            break
        elif response == "b":
            print("Your goal is to line up three pieces in a row. Player one places X, while player two places O")
            print("Format your responses as a column then a row, with a space in between. For example, you could play \"1 2\"")
            print("Have fun!")
        elif response == "c":
            print("Goodbye")
            quit()
        else:
            print("Invalid option")


def result_check():
    if board[0][0] == board[0][1] == board[0][2] != "-":
        return True
    if board[1][0] == board[1][1] == board[1][2] != "-":
        return True
    if board[2][0] == board[2][1] == board[2][2] != "-":
        return True
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True

def get_moves(t):
    while True:
        try:
            move = input("Where would you like to place your piece?")
            x = int(move[0])
            y = int(move[2])
        except Exception:
            print("Please input two coordinates of where you would like the piece to be placed, such as \"2 1\"")
        else:
            if 0 < x < 4 and 0 < y < 4 and board[y - 1][x - 1] == "-":
                board[y-1][x-1] = "X" if t == 1 else "O"
                break
            else:
                print("A piece already exists on that square or the coordinates are out of bounds")


def print_board():
    for i in board:
        for x in i:
            print(x, end="   ")
        print("\n")

main()
