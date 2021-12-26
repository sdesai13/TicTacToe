#!/usr/bin/env python
# coding: utf-8

# In[15]:


from IPython.display import clear_output
 
def display_board(board):
    
    clear_output()
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("___ ___ ___")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___ ___ ___")
    print(f" {board[0]} | {board[1]} | {board[2]} ")


# In[60]:


#row1= "         "
#defaultrow= "012345678"

#display_board(row1)


# In[91]:


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
        


# In[92]:


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


# In[85]:


def boardchoicep1 ():
    acceptablechoices = ["0","1","2","3","4","5","6","7","8"]
    choice = "invalid"
    
    while choice not in acceptablechoices:
        choice = input ("Player1, what position on the board would you like to place your symbol?: ")
        
        if choice not in acceptablechoices:
            print ("Sorry, your choice was invalid.")
            
        else:
            continue
       
    return int(choice)


# In[86]:


def boardchoicep2 ():
    acceptablechoices = ["0","1","2","3","4","5","6","7","8"]
    choice = "invalid"
    
    while choice not in acceptablechoices:
        choice = input ("Player2, what position on the board would you like to place your symbol?: ")
        
        if choice not in acceptablechoices:
            print ("Sorry, your choice was invalid.")
            
        else:
            continue
       
    return int(choice)


# In[30]:




# In[41]:


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
        
    
    


# In[53]:


def winnercheck (board):
    
   #checks which of the 8 winning combinations occured, and outputs the combination code for that combo. 
    
   
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
    
 
        


# In[96]:


def tictactoe ():
    winningcombo = ""
    player1symbol = symbolchoicep1()
    
    player2symbol = symbolchoicep2()
    player1marker = ""
    player2marker = ""
    gamestatus = 2
    board = "         "
    
    
    while gamestatus == 2:
       
        display_board(board)
        player1marker = boardchoicep1()
        board = board[:player1marker] + player1symbol + board[player1marker+1:]
        display_board (board)
        gamestatus = gamecheck(board)
        player2marker = boardchoicep2()
        board = board[:player2marker] + player2symbol + board[player2marker+1:]
        display_board (board)
        gamestatus = gamecheck(board)
    
    
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
    
    
        
        
  
        
        
        
    
   


# In[97]:


tictactoe()



# In[ ]:




