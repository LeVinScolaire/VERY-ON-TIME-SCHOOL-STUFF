board = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "]
    ]

first_marker = "X" #determines the marker for player 1
second_marker = "O" #determines the marker for player 2
win = False #win/loss variable - if its true, the game should stop
current_player = "Player One" #determines who needs to play

#This function prints the board.
#Run this function to check it out!
def print_board():
    print(" 1 2 3 4 5 6 7")
    for i in range(len(board)):
        for j in board[i]:
            print(j+"|",end="")
        print("")
print_board()

def player_one():
    global board
    global current_player
    marker = "X"
    ask = int(input("What column would you like to play? "))
    if board[0][ask] != " ":
        print("Play another column")
    for i in range(6,0,-1):
        if board[i][ask] != " ":
            continue
        else:
            board[i][ask] = marker
            break
    print_board()
    win_lose()
    current_player = "Player Two"

def player_two():
    global board
    global current_player
    marker = "O"
    ask = int(input("What column would you like to play? "))
    if board[0][ask] != " ":
        print("Play another column")
    for i in range(6,0,-1):
        if board[i][ask] != " ":
            continue
        else:
            board[i][ask] = marker
            break
    print_board()
    win_lose()
    current_player = "Player One"


#this literally serves no purpose so i'm removing it
"""
def insert_piece():
    #you can use this function to insert the piece onto the board
"""

def win_lose():
    global win
    XCounter = 0
    OCounter = 0
    #For Horizontal Victories
    for i in range(7):
        XCounter = 0
        OCounter = 0
        for j in range(7):
            if board[i][j] == "X":
                XCounter += 1
                OCounter = 0
            elif board[i][j] == "O":
                OCounter += 1
                XCounter = 0
            else:
                XCounter = 0
                OCounter = 0
            if XCounter == 4:
                print("Player One Wins!")
                win = True
                break
            elif OCounter ==4:
                print("Player Two Wins!")
                win = True
                break
            else:
                continue
                

#This runs the game... be careful running this (infinite loop)
while win != True:
    if current_player == "Player One":
        player_one()
    if current_player == "Player Two":
        player_two()



    
