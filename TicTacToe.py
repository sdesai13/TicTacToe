


from IPython.display import clear_output
 
# display_board(board) is a function that is used to continously display the game board. It uses the IPython module, and
# uses string data manipulation to create the game board.
    
def display_board(board):
    
    clear_output()
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("___ ___ ___")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___ ___ ___")
    print(f" {board[0]} | {board[1]} | {board[2]} ")



# symbolchoicep1 is a function that is used to collect what symbol each player wants to use in the game. The two options
# are "X" or "O". Players can manually choose which symbol each one is, or if they want to they can both play with the same symbol.

def symbolchoicep1 ():
    acceptablesymbols = ["X", "O"]
    choice = "Invalid"
    
    while choice not in acceptablesymbols:
        
        choice = input ("Player1, what symbol would you like to place on the board?: ")
        
        if choice not in acceptablesymbols:
            print ("Sorry, your choice was invalid.")
        
        else:
            continue 
    
    return choice 
        


# symbolchoicep2 is a function that is used to collect what symbol each player wants to use in the game. The two options
# are "X" or "O". Players can manually choose which symbol each one is, or if they want to they can both play with the same symbol.


def symbolchoicep2 ():
    acceptablesymbols = ["X", "O"]
    choice = "Invalid"
    
    while choice not in acceptablesymbols:
        
        choice = input ("Player2, what symbol would you like to place on the board?: ")
        
        if choice not in acceptablesymbols:
            print ("Sorry, your choice was invalid.")
        
        else:
            continue 
    
    return choice  


# gamecheck(board) is a function that consumes a game board, and checks whether the "3 in a row" condition for tic tac toe
# has been met, or if all 9 index slots on the board are completely filled. returns key code values symbolizing the result.
# a return value of 0 means "3 in a row" condition is met, a return value of 1 means all 9 index spots are filled, and a return value of 2 means the game must continue. 


def gamecheck (board):
    
    #return of 0 means we have a three in row
    #return of 1 means all 9 board spots are filled. game must end
    #return of 2 means neither condition is met, keep playing!
    
   
    if (board [6] == "X" or board[6] == "O") and (board [6] == board [3] == board [0]):
        return 0
    elif (board [7] == "X" or board[7] == "O") and (board[7] == board [4] == board [1]):
        return 0
    elif (board [8] == "X" or board[8] == "O") and (board[8] == board [5] == board [2]):
        return 0
    elif (board [6] == "X" or board[6] == "O") and (board[6] == board [7] == board [8]):
        return 0
    elif (board [3] == "X" or board[3] == "O") and (board[3] == board [4] == board [5]):
        return 0
    elif (board [0] == "X" or board[0] == "O") and (board[0] == board [1] == board [2]):
        return 0
    elif (board [6] == "X" or board[6] == "O") and (board[6] == board [4] == board [2]):
        return 0
    elif (board [0] == "X" or board[0] == "O") and (board[0] == board [4] == board [8]):
        return 0
    
 
    elif board.find(" ") == -1:
        return 1
    else:
        return 2
        
    
    
# winnercheck (board): is a function that checks which of the 8 winning combinations occured, and outputs the combination code for that combo. 
    


def winnercheck (board):
    
  
    
   
    if (board [6] == "X" or board[6] == "O") and (board [6] == board [3] == board [0]):
        return "c1"
    elif (board [7] == "X" or board[7] == "O") and (board[7] == board [4] == board [1]):
        return "c2"
    elif (board [8] == "X" or board[8] == "O") and (board[8] == board [5] == board [2]):
        return "c3"
    elif (board [6] == "X" or board[6] == "O") and (board[6] == board [7] == board [8]):
        return "c4"
    elif (board [3] == "X" or board[3] == "O") and (board[3] == board [4] == board [5]):
        return "c5"
    elif (board [0] == "X" or board[0] == "O") and (board[0] == board [1] == board [2]):
        return "c6"
    elif (board [6] == "X" or board[6] == "O") and (board[6] == board [4] == board [2]):
        return "c7"
    elif (board [0] == "X" or board[0] == "O") and (board[0] == board [4] == board [8]):
        return "c8"
    
# tictactoe() is the game itself. running the function tictactoe() will initiate gameplay. The game will prompt player1 and player 2 to pick their respective symbols, the game loop will continue until either "3 in a row" is met or until all 9 board spots are filled and the game ends in a tie. To manually exit the game, the user can stop the script. 
        

def tictactoe ():
    winningcombo = ""
    player1symbol = symbolchoicep1()
    
    player2symbol = symbolchoicep2()
    player1marker = ""
    player2marker = ""
    gamestatus = 2
    board = "         "
  
    choicemarker = ""
    
    acceptablechoices = ["0","1","2","3","4","5","6","7","8"]
    
    # boardchoicep1() is a nested function used to collect the desired index position to put their symbol each turn for player 1.
    
    def boardchoicep1 ():
       
   
        choice = "invalid"
    
        while choice not in acceptablechoices:
            choice = input ("Player1, what position on the board would you like to place your symbol?: ") 
        
            if choice not in acceptablechoices: 
                print ("Sorry, your choice was invalid.")
            
            else:
                continue
        
        return int(choice)
    
     # boardchoicep2() is a nested function used to collect the desired index position to put their symbol each turn for player 1
    
    def boardchoicep2 ():
       
   
        choice = "invalid"
    
        while choice not in acceptablechoices:
            choice = input ("Player2, what position on the board would you like to place your symbol?: ") 
        
            if choice not in acceptablechoices: 
                print ("Sorry, your choice was invalid.")
            
            else:
                continue
        
        return int(choice)

            
       
    
    
    while gamestatus == 2:
       
        # display_board(board)
        
        player1marker = boardchoicep1()
        board = board[:player1marker] + player1symbol + board[player1marker+1:]
        choicemarker = str(player1marker)
        display_board (board)
        gamestatus = gamecheck(board)
        
        if gamestatus != 2:
            break
        else:
            pass 
            
        
        if len (acceptablechoices) > 1:
            acceptablechoices.remove(choicemarker)
        else:
            pass
            
        
        
        player2marker = boardchoicep2()
        board = board[:player2marker] + player2symbol + board[player2marker+1:]
        choicemarker = str(player2marker)
        display_board (board)
        gamestatus = gamecheck(board)
        
        if gamestatus != 2:
            break
        else:
            pass 
            
       
        if len (acceptablechoices) > 1:
            acceptablechoices.remove(choicemarker)
        else:
            pass
        
        
    
    
    if gamestatus == 1:
        print ("All 9 positions have been filled. Game is a tie.")
    elif gamestatus == 0:
        if winnercheck(board) == "c1":
            print (f'The player with the symbol {board[6]} won!')
        elif winnercheck(board) == "c2":
            print (f'The player with the symbol {board[7]} won!')
        elif winnercheck(board) == "c3":
            print (f'The player with the symbol {board[8]} won!')
        elif winnercheck(board) == "c4":
            print (f'The player with the symbol {board[6]} won!')
        elif winnercheck(board) == "c5":
            print (f'The player with the symbol {board[3]} won!')
        elif winnercheck(board) == "c6":
            print (f'The player with the symbol {board[0]} won!')
        elif winnercheck(board) == "c7":
            print (f'The player with the symbol {board[4]} won!')
        elif winnercheck(board) == "c8":
            print (f'The player with the symbol {board[0]} won!')
    
    
        
tictactoe()













