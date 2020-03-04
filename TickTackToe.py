board = [' ' for i in range(0,9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[6],board[7],board[8])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[0],board[1],board[2])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def draw():
    if ' ' not in board:
        return True
    else :
        return False

while True :

    
    
    print_board()
    while True:
        
        print("Player 1")

        while True:
            choice = int(input("Enter Your Move (1-9): ").strip())
            if choice <= 0 or choice >= 10:
                pass
            else:
                break
    
        if board[choice - 1] == " " :
            board[choice - 1] = "X"
            break
        else :
            print("Enter Another Move")
            pass
    
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or 
        board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or 
        board[6] == 'X' and board[7] == 'X' and board[8] == 'X' or 
        board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or 
        board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or 
        board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or 
        board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or 
        board[2] == 'X' and board[4] == 'X' and board[6] == 'X') :
        print_board()
        print("Player 1  WON !!!")
        break

    elif draw():
        print_board()
        print("DRAW")
        break


    
    print_board()
    while True:
        
        print("Player 2")

        while True:
            choice = int(input("Enter Your Move (1-9): ").strip())
            if choice <= 0 or choice >= 10:
                pass
            else:
                break
        
        if board[choice - 1] == " " :
            board[choice - 1] = "O"
            break
        else :
            print("Enter Another Move")
            pass

    if (board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or 
        board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or 
        board[6] == 'O' and board[7] == 'O' and board[8] == 'O' or 
        board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or 
        board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or 
        board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or 
        board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or 
        board[2] == 'O' and board[4] == 'O' and board[6] == 'O') :
        print_board()
        print("Player 2  WON !!!")
        break

    elif draw():
        print_board()
        print("DRAW")
        break
