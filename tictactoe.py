#### TicTacToe with 1 or 2 player modes with computer random move generator
#### For Terminal Use- Removed clear_output module used with ipython and replaced with: def cls(): print "\n" * 100
#### A Programme written by James W Heath

import random

def main():
    
    title = '''
	I=====I I=====I ======I
	   I       I    I
	   I       I    I
	   I    I=====I ======I
	I=====I ======= ======I
	   I    I     I I
	   I    I=====I I
	   I    I     I ======I
	I=====I ======= ======I
	   I    I     I I___
	   I    I     I I
	   I    ======= ======I
	
	'''
    print(title)
    input('Press ENTER to begin, or press CTRL-C to Cancel')
        
    def play(): # Contains the game play functions
        
        boardspaces = [1,2,3,4,5,6,7,8,9] # List of avaialble spaces as integers
        board = ['1','2','3','4','5','6','7','8','9'] # Lists the board spaces as strings for tiles numbers/markers 
        
        def cls(): # Clears the screen to make it less cluttered
            print("\n" * 100)

        def displayboard():# Displays board using list index
            cls()
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
            print('---|---|---')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
            print('---|---|---')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])

        def wincheck():# Checks for a winner or draw, used after each turn. 
            if board[0] == board[1] == board[2]:
                print("%s IS THE WINNER!" %(board[0]))
                endgame()
            elif board[3] == board[4] == board[5]:
                print("%s IS THE WINNER!" %(board[3]))
                endgame()
            elif board[6] == board[7] == board[8]:
                print("%s IS THE WINNER!" %(board[6]))
                endgame()
            elif board[6] == board[3] == board[0]:
                print("%s IS THE WINNER!" %(board[6]))
                endgame()
            elif board[7] == board[4] == board[1]:
                print("%s IS THE WINNER!" %(board[7]))
                endgame()
            elif board[8] == board[5] == board[2]:
                print("%s IS THE WINNER!" %(board[8]))
                endgame()
            elif board[6] == board[4] == board[2]:
                print("%s IS THE WINNER!" %(board[6]))
                endgame()
            elif board[0] == board[4] == board[8]:
                print("%s IS THE WINNER!" %(board[0]))
                endgame()
            elif boardspaces == []:
                print('DRAW!')
                endgame()
        
        def xturn(): # Player X turn system
            while True:
                x = (input("Player X's turn: "))
                if x in board:
                    index = board.index(x)     
                    board.remove(x)
                    board.insert(index, 'X')
                    boardspaces.remove(int(x))
                    displayboard()
                    wincheck()
                    break
                else:
                    displayboard()
                    print('Invalid Input')           

        def oturn(): # Player O turn system
            while True:
                x = (input("Player O's turn: "))
                if x in board:
                    index = board.index(x)    
                    board.remove(x)
                    board.insert(index, 'O')
                    boardspaces.remove(int(x))
                    displayboard()
                    wincheck()
                    break
                else:
                    displayboard()
                    print('Invalid Input')
                    
        def compturn(): # Randomly assigned 'O' markers to play against
            x = random.choice(boardspaces)
            index = board.index(str(x))
            board.remove(str(x))
            board.insert(index, 'O')
            boardspaces.remove(x)
            displayboard()
            wincheck()

        def twoplayer():# Determines which marker starts
            randomchoice = random.choice
            while True:       
                displayboard()
                answer = input("Who will start? Press X or O or R for Random!\n").upper()
                cls()
                if answer == 'X':
                    displayboard()
                    while True:
                        xturn()
                        oturn()
                elif answer == 'O':
                    displayboard()
                    while True:
                        oturn()
                        xturn()         
                elif answer == 'R': # Determins a random marker to start 
                    choices = ['x', 'o']
                    randomchoice = random.choice(choices)
                    if randomchoice == 'x':
                        displayboard()
                        while True:
                            xturn()
                            oturn()
                    else:
                        displayboard()
                        while True:
                            oturn()
                            xturn()   

        def oneplayer(): # Selects at random which marker goes first
            choices = ['player', 'comp']
            randomchoice = random.choice(choices)
            if randomchoice == 'player':
                displayboard()
                while True:
                    xturn()
                    compturn()
            else:
                displayboard()
                while True:
                    compturn()
                    xturn()                          
                            
        def playmode(): # requests input for either two player or against computer
            while True:    
                cls()
                print(title)
                answer = input("Enter '1' for Single Player\nEnter '2' for Two Player\n")
                if answer == '1':
                    oneplayer()
                elif answer == '2':       
                    twoplayer()

        def endgame(): # After a win or draw resets the game loop
            restart = input('Press ENTER To Play Again or CTRL-C to Exit!\n')
            play()

        playmode()
        
    play()
    
if __name__ == "__main__":
    main()

