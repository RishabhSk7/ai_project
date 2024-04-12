import os
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player = 1

# Win Flags to look at the outcomes of the match

Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running
Mark = "X"

# Function ‘DrawBoard’ to define an interface for players to see the board with %c as place holders for the marks that will be made during the game.


def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print(" | | ")


# Function ‘CheckPosition’ to check whether the chosen position on the board is free or pre occupied with a mark.


def CheckPosition(x):
    if board[x] == " ":
        return True
    else:
        return False


# Function ‘CheckWin’ to check for a possibility of a game win or a game tie and to check whether the game has ended or should still run ahead.


def CheckWin():
    global Game

    if board[1] == board[2] and board[2] == board[3] and board[1] != " ":
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != " ":
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != " ":
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != " ":
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != " ":
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != " ":
        Game = Win
    elif (
        board[1] != " "
        and board[2] != " "
        and board[3] != " "
        and board[4] != " "
        and board[5] != " "
        and board[6] != " "
        and board[7] != " "
        and board[8] != " "
        and board[9] != " "
    ):
        Game = Draw
    else:
        Game = Running


print("Tic-Tac-Toe Game Designed By Ayush Pawar")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)

while Game == Running:
    os.system("cls")
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = "X"
    else:
        print("Player 2's chance")
        Mark = "O"

    choice = int(input("Enter the position between [1-9] where you want to mark: "))
    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

    os.system("cls")
    DrawBoard()

    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
