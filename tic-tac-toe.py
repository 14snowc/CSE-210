'''
Solo Checkpoint 02
Author: Codie Snow
'''

def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    #Make some starting variables
    draw = False
    is_win = False
    victory_info = {
        'player' : '',
        'method' : [],
    }
    player = ['x', 'o']
    current = 0
    # assign/get the first player
    player[0] = input("Enter the character for the first player: ").strip()[:1]
    player[1] = input("Enter a diffrent character for the second player: ").strip()[:1]
    while player[0] == "" or player[1] == "" or player[0] == player[1]:
        print("Invalid inputs.")
        player[0] = input("Enter the character for the first player: ").strip()[:1]
        player[1] = input("Enter a diffrent character for the second player: ").strip()[:1]

    # create a board
    board = create_board()
    # loop if there isn't a winner
    while is_win == False:
        pass
        # allow the player to make a move
        make_move(player, board, current)

        #check for victory
        is_win, victory_info = is_winner(board, victory_info, is_win)

        #check if draw
        draw = is_draw(board, player)

        #if it is a draw make a new board
        if draw == True:
            print("Draw, making a new game.")
            board = create_board()
            draw = False
        
        # pick the next player
        current = next_player(current)

    # display the final board
    display_board(board)
    # show message for winner and thanks for playing
    if victory_info['player'] != '':
        print (f"The winner is {victory_info['player']}.")
        for victory_number in range(1, len(victory_info['method']) + 1):
            print(victory_info['method'][victory_number - 1])
    print("Thanks for playing")
    pass

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    #To do this I think using a list within a list would work. Space will be blank
    row_column_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return row_column_list

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    for row in range(1, 4):
        print(f"{row}", end= " | ")
        for column in range(1, 4):
            if column != 3:
                print(f"{board[row-1][column-1]}", end=" | ")
            else:
                print(f"{board[row-1][column-1]}")
        print("--------------")
    print("/ | 1 | 2 | 3")

def is_draw(board, player):
    ''' return: True if board is a draw, False if board is still playable '''
    draw = True
    for row in range(1, 4):
        for column in range(1, 4):
            test = board[row-1][column-1]
            if test == ' ':
                draw = False
    return draw

def is_winner(board, victory_info, is_win):
    ''' return: True if someone won, False if there is no winner '''
    
    #check row/column victory
    for row in range (1, 4):
        if board[row-1][0] != ' ' and board[row-1][0] == board[row-1][1] == board[row-1][2]:
            victory_info['player'] = board[row-1][0]
            victory_info['method'].append(f"Row {row} victory.")
            is_win = True
    for column in range (1, 4):
        if board[0][column-1] != ' ' and board[0][column-1] == board[1][column-1] == board[2][column-1]:
            victory_info['player'] = board[0][column-1]
            victory_info['method'].append(f"Column {column} victory.")
            is_win = True

    #Check diagnal victory
    if board[0][0] != ' ' and board [0][0] == board[1][1] == board[2][2]:
        victory_info['player'] = board[0][0]
        victory_info['method'].append(f"Top left diagnal victory.")
        is_win = True
    if board[0][2] != ' ' and board [0][2] == board[1][1] == board[2][0]:
        victory_info['player'] = board[0][2]
        victory_info['method'].append(f"Bottom left diagnal victory.")
        is_win = True

    return is_win, victory_info

def make_move(player, board, current):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    valid_move = False
    user_input = [0, 0]
    while valid_move == False:
        try:
            #I display a board here so if multiple invalid inputs are made the board will still be easy to see
            display_board(board)
            user_input[0] = int(input("Please input a row: ")) - 1
            user_input[1] = int(input("Please input a column: ")) - 1
            if user_input[0] > 2 or user_input[1] > 2:
                print("Please pick a lower number.")
            elif user_input[0] < 0 or user_input[1] < 0:
                print("Please pick a higher number.")
            elif board[user_input[0]][user_input[1]] != ' ':
                print("Space already taken, please pick another space.")
            else:
                valid_move = True
                board[user_input[0]][user_input[1]] = player[current]
        except:
            print("Invalid input, please type a number between 1 - 3")

def next_player(current):
    ''' return: 1 if current is 0, otherwise 0 '''
    if current == 0:
        current = 1
    else:
        current = 0
    return current
"""
def ai(player, board, current):
    pass
    #We will use a score method to help make the code easier. AI markers will be worth 1 point, blanks are 0, and enemies are -1. if a 2 is found the game can be won.
    #we want the AI to check for victory first

    
    score = 0
    optional_moves = []
    for row in range (1, 4):
        for item in board[row]:
            #find a way to check the ai
            if item == player[current]:
                score  += 1
            elif item == player[-(current + 1)]:
                score -= 1
        if score == 2:
        #finish this in the future, got other assignments to do
    """
                


# run main if this has been called from the command line
if __name__ == "__main__":
    main()