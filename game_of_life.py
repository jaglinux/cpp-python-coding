def game_of_life(board):
    row_max = len(board)
    col_max = len(board[0])

    def find_ones(i, j):
        ones = 0
        if i-1 >= 0:
            if (board[i-1][j] & 1) == 1:
                ones+=1
            if j-1 >= 0 and (board[i-1][j-1] & 1) == 1:
                ones+=1
            if j+1 < col_max and (board[i-1][j+1] & 1) == 1:
                ones+=1
        if i+1 < row_max:
            if (board[i+1][j] & 1) == 1:
                ones+=1
            if j-1 >= 0 and (board[i+1][j-1] & 1) == 1:
                ones+=1
            if j+1 < col_max and (board[i+1][j+1] & 1) == 1:
                ones+=1
        if j-1 >= 0 and (board[i][j-1] & 1) == 1:
            ones+=1
        if j+1 < col_max and (board[i][j+1] & 1) == 1:
            ones+=1
        return ones

    for i in range(row_max):
        for j in range(col_max):
            ones = find_ones(i, j)
            if (board[i][j] & 1) == 0:
                # Check if it can be alive
                if ones == 3:
                    board[i][j] = 2
            else:
                if ones == 2 or ones == 3:
                    board[i][j] = 3

    for i in range(row_max):
        for j in range(col_max):
            if board[i][j] > 1:
                board[i][j] = 1
            else:
                board[i][j] = 0

if __name__ == '__main__':
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    game_of_life(board)
    print(board)
# [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
