

def print_board(board):
    for i in range(4):
        if(i==0):
            print("-----------------------------")
        print("| ", board[i][0], ' | ', board[i][1], " | ", board[i][2], " | ", board[i][3], " |")
        print("-----------------------------")

def check_winner(board,times):
    if (times == 7):
        for i in range(4):
            for j in range(4):
                if (board[i][j]) !="XX":
                    if (j < 3 and board[i][j + 1]  =="XX") and (i<3 and board[i+1][j]  =="XX"):
                        return 1
    return 0

def update(board, num):
    for i in range(4):
        for j in range(4):

                if int(board[i][j]) == int(num):
                    board[i][j] = "XX"
                    return


def validate(board, x, y):
    for i in range(4):
        for j in range(4):
            if board[i][j] != "XX":
                if board[i][j].isdigit() and int(board[i][j]) == int(x):
                    if (j < 3 and board[i][j + 1].isdigit() and int(board[i][j + 1]) == int(y)) or \
                            (j > 0 and board[i][j - 1].isdigit() and int(board[i][j - 1]) == int(y)) or \
                            (i < 3 and board[i + 1][j].isdigit() and int(board[i + 1][j]) == int(y)) or \
                            (i > 0 and board[i - 1][j].isdigit() and int(board[i - 1][j]) == int(y)):
                        return 1
    return 0

def main():
    board = [["01", "02", "03", "04"], ["05", "06", "07", "08"], ["09", "10", "11", "12"], ["13", "14", "15", "16"]]
    times=0
    while(times<8):
        print_board(board)
        x = int(input("player 1 choose the first square : "))
        y = int(input("player 1 choose the second square : "))
        while not validate(board,x,y):
            x = int(input("player 1 choose the first square : "))
            y = int(input("player 1 choose the second square : "))
        update(board, x)
        update(board, y)
        times += 1
        if(check_winner(board,times)):
            print("player 1 is the winner")
            return
        print_board(board)
        x = int(input("player 2 choose the first square : "))
        y = int(input("player 2 choose the second square : "))
        while not validate(board,x,y):
            x = int(input("player 2 choose the first square : "))
            y = int(input("player 2 choose the second square : "))
        update(board, x)
        update(board, y)
        times += 1
        if (check_winner(board, times)):
            print("player 2 is the winner")
            return
    print("player 2 is the winner")
    return


main()