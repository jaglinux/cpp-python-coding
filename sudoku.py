def is_board_full(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True

def get_pos_values(board, y ,z):
    possible_values={}
    result=[]
    for j in range(9):
        if board[y][j] != 0:
            possible_values[board[y][j]] = True
    for i in range(9):
        if board[i][z] != 0:
            possible_values[board[i][z]] = True
    m = n = 0
    if y in [0,1,2]:
        m = 0
    elif y in [3,4,5]:
        m = 3
    else:
        m = 6
    if z in [0,1,2]:
        n = 0
    elif z in [3,4,5]:
        n = 3
    else:
        n = 6

    for i in range(m ,3):
        for j in range(n, 3):
            if board[i][j] != 0:
                possible_values[board[i][j]] = True
    for i in range(1, 10):
        if i not in possible_values:
            result.append(i)
    return result

def sudoku(board):
    if is_board_full(board):
        print('Result is ')
        for i in board:
            print(i)
        exit()
    y = z = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y = i
                z = j
                break

    possible_values = get_pos_values(board, y, z)
    for v in possible_values:
        board[y][z] = v
        sudoku(board)
    board[y][z] = 0


def main():
    SudokuBoard = [[0 for x in range(9)] for x in range(9)]
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0
    SudokuBoard[0][3] = 3
    SudokuBoard[0][4] = 0
    SudokuBoard[0][5] = 0
    SudokuBoard[0][6] = 2
    SudokuBoard[0][7] = 0
    SudokuBoard[0][8] = 0
    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 0
    SudokuBoard[1][2] = 0
    SudokuBoard[1][3] = 0
    SudokuBoard[1][4] = 0
    SudokuBoard[1][5] = 8
    SudokuBoard[1][6] = 0
    SudokuBoard[1][7] = 0
    SudokuBoard[1][8] = 0
    SudokuBoard[2][0] = 0
    SudokuBoard[2][1] = 7
    SudokuBoard[2][2] = 8
    SudokuBoard[2][3] = 0
    SudokuBoard[2][4] = 6
    SudokuBoard[2][5] = 0
    SudokuBoard[2][6] = 3
    SudokuBoard[2][7] = 4
    SudokuBoard[2][8] = 0
    SudokuBoard[3][0] = 0
    SudokuBoard[3][1] = 4
    SudokuBoard[3][2] = 2
    SudokuBoard[3][3] = 5
    SudokuBoard[3][4] = 1
    SudokuBoard[3][5] = 0
    SudokuBoard[3][6] = 0
    SudokuBoard[3][7] = 0
    SudokuBoard[3][8] = 0
    SudokuBoard[4][0] = 1
    SudokuBoard[4][1] = 0
    SudokuBoard[4][2] = 6
    SudokuBoard[4][3] = 0
    SudokuBoard[4][4] = 0
    SudokuBoard[4][5] = 0
    SudokuBoard[4][6] = 4
    SudokuBoard[4][7] = 0
    SudokuBoard[4][8] = 9
    SudokuBoard[5][0] = 0
    SudokuBoard[5][1] = 0
    SudokuBoard[5][2] = 0
    SudokuBoard[5][3] = 0
    SudokuBoard[5][4] = 8
    SudokuBoard[5][5] = 6
    SudokuBoard[5][6] = 1
    SudokuBoard[5][7] = 5
    SudokuBoard[5][8] = 0
    SudokuBoard[6][0] = 0
    SudokuBoard[6][1] = 3
    SudokuBoard[6][2] = 5
    SudokuBoard[6][3] = 0
    SudokuBoard[6][4] = 9
    SudokuBoard[6][5] = 0
    SudokuBoard[6][6] = 7
    SudokuBoard[6][7] = 6
    SudokuBoard[6][8] = 0
    SudokuBoard[7][0] = 0
    SudokuBoard[7][1] = 0
    SudokuBoard[7][2] = 0
    SudokuBoard[7][3] = 7
    SudokuBoard[7][4] = 0
    SudokuBoard[7][5] = 0
    SudokuBoard[7][6] = 0
    SudokuBoard[7][7] = 0
    SudokuBoard[7][8] = 0
    SudokuBoard[8][0] = 0
    SudokuBoard[8][1] = 0
    SudokuBoard[8][2] = 9
    SudokuBoard[8][3] = 0
    SudokuBoard[8][4] = 0
    SudokuBoard[8][5] = 5
    SudokuBoard[8][6] = 0
    SudokuBoard[8][7] = 0
    SudokuBoard[8][8] = 0
    for i in SudokuBoard:
        print(i)
    sudoku(SudokuBoard)
    # file.close()


if __name__ == "__main__":
    main()
