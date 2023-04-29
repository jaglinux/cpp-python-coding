inf = float("inf")

def bfs(grid):
    row_max, col_max = len(grid), len(grid[0])
    q = []
    for i in range(row_max):
        for j in range(col_max):
            if grid[i][j] == 0:
                q.append((i,j))

    def move(i, j):
        if i < 0 or i == row_max or j < 0 or j == col_max or grid[i][j] == -1 or (i,j) in q:
            return
        if grid[i][j] == inf:
            q.append((i,j))

    distance = 0
    while len(q):
        for _ in range(len(q)):
            i,j = q.pop(0)
            grid[i][j] = distance
            move(i, j-1)
            move(i, j+1)
            move(i-1, j)
            move(i+1, j)
        distance += 1

grid = [ [inf, -1,   0,  inf],
         [inf, inf, inf, -1],
         [inf, -1,  inf, -1],
         [0,   -1,  inf, inf] ]

bfs(grid)

print(grid)
# [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
