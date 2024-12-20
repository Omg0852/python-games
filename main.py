import random

# Initializing  the board
# at the starting of the game it will be a list of 9 blanks[' ',' ',...]
# so  far the game progress the blanks will be replaced by 'X' or 'O' until all the blanks are replaced
board = [" " for _ in range(9)]

# Score Variable to Keep Track of the scoreCard

player_score = 0
computer_score = 0

print(""" 
██████╗  █████╗ ███╗   ███╗███████╗         ██████╗ ███╗   ██╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝        ██╔═══██╗████╗  ██║
██║  ███╗███████║██╔████╔██║█████╗          ██║   ██║██╔██╗ ██║
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          ██║   ██║██║╚██╗██║
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        ╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝         ╚═════╝ ╚═╝  ╚═══╝

                                                              \n
""")


# This function place the Board


def print_board():
    for i in range(3):
        print(" ❕".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("➖➕➖➕➖")


# As the Name Suggest it Check for the winner Win conditions variable consist all the winig combinations
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# If all the 9 boxes are filled this suggest the game is tied
# this function return true or false
def is_full():
    return " " not in board


# function to player on the behalf of the Computer or the BOT
def get_computer_move(player, opponent):
    # Try to win

    # method place the temporary Move into imagination if by that move made is wining then the computer return move (location) else left it blank
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(player):
                return i
            board[i] = " "

    # Try to block opponent
    #
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent  # considered move of the player imagined by the computer
            if check_winner(opponent):  # if player is wining then computer move is what he imagined of player
                board[i] = player
                return i
            board[i] = " "
    # Choose random move

    # if both the above conditions end in a blank
    # the computer play the random move .
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            return move


def play_game():
    global computer_score, player_score

    player_symbol = input("Choose your symbol (X/O  :'X' always made's first move): ").upper()

    while player_symbol not in ["X", "O"]:
        player_symbol = input("Invalid choice. Choose X or O: ").upper()
    computer_symbol = "O" if player_symbol == "X" else "X"
    current_player = "X"

    while True:
        print_board()
        if current_player == player_symbol:  # checking for if it's players turn or the computer's
            try:
                move = int(input(f"Player {player_symbol}, enter your move (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = player_symbol  # if the location is blank then placing the Symbol there
                    if check_winner(player_symbol):  # check if the player wins and take appropriate action
                        print_board()
                        print(f"Player {player_symbol} wins!")
                        player_score += 1
                        break
                    elif is_full():  # checking if it's a tie
                        print_board()
                        print("The game is a tie!")
                        break
                    current_player = computer_symbol  # after the player turn is over now it's computers turn
                else:
                    print("Invalid move, try again.")

            # Exception handling block if the user Entered Wrong input's or Move
            except (ValueError, IndexError):
                print("Invalid input, please enter a number between 1 and 9.")

            # Computers turn
        else:
            move = get_computer_move(computer_symbol, player_symbol)
            board[move] = computer_symbol
            print(f"Computer chose position {move + 1}")
            if check_winner(computer_symbol):
                print_board()
                print(f"Computer ({computer_symbol}) wins!")
                computer_score += 1
                break
            elif is_full():
                print_board()
                print("The game is a tie!")
                break
            current_player = player_symbol


if __name__ == "__main__":
    # providing the player a functionality of series of game
    play = True
    while play:
        play_game()
        play = bool(int((input("Do You Want To Play Another Game : Yes -> 1/ NO->0 : "))))
        if play:
            board = [" " for _ in range(9)]
        else:
            print(""" 
 ██████╗  █████╗ ███╗   ███╗███████╗         ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝        ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗          ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝         ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                              \n\n""")
            print(f"\n\n【F】【i】【n】【a】【l】\n░S░c░o░r░e░B░o░a░r░d░ : \t𝓟ℒ𝓐Ⴘ𝓔ℛ : {player_score}\n\t\t\t\t\t\t\t𝓒𝓸𝓶𝓹𝓾𝓽𝓮𝓻: {computer_score}")


