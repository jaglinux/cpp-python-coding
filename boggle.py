def find_neigh(grid, i, j, flag, a):
    result=[]
    if i > 0:
        if grid[i-1][j] == a and not flag[i-1][j]:
            result.append((i-1,j))
        if j+1 < 4:
            if grid[i-1][j+1] == a and not flag[i-1][j+1]:
                result.append((i-1, j+1))
        if j > 0:
            if grid[i-1][j-1] == a and not flag[i-1][j-1]:
                result.append((i-1, j-1))
    if j+1 < 4:
        if grid[i][j+1] == a and not flag[i][j+1]:
            result.append((i, j+1))
    if j > 0:
        if grid[i][j-1] == a and not flag[i][j-1]:
            result.append((i, j-1))
    if i+1 < 4:
        if grid[i+1][j] == a and not flag[i+1][j]:
            result.append((i+1, j))
        if j+1 < 4:
            if grid[i+1][j+1] == a and not flag[i+1][j+1]:
                result.append((i+1, j+1))
        if j > 0:
            if grid[i+1][j-1] == a and not flag[i+1][j-1]:
                result.append((i+1, j-1))
    return result

def recurse(grid, search, i, j, k, flag):
    flag[i][j] = True
    if k+1 == len(search):
        return True
    if flag[i][j] == False:
        return False
    if grid[i][j] != search[k]:
        return False
    neighs = find_neigh(grid, i, j, flag, search[k+1])
    for neigh in neighs:
        result = recurse(grid, search, neigh[0], neigh[1], k+1, flag)
        if result == True:
            return True
        else:
            continue
    return False
    
def reset_flag(flag):
    for i in range(4):
        for j in range(4):
            flag[i][j] = False
            
def func(grid, search):
    flag = []
    for i in range(4):
        flag.append([])
        for j in range(4):
            flag[i].append(False)
            
    for i in range(4):
        for j in range(4):
            if grid[i][j] == search[0]:
                res = recurse(grid, search, i, j, 0, flag)
                if res == True:
                    return True
                else:
                    reset_flag(flag)
    return False

if __name__ == '__main__':
    grid= [
        ['E', 'S', 'A', 'T'],
        ['A', 'T', 'D', 'F'],
        ['O', 'T', 'I', 'E'],
        ['K', 'L', 'M', 'U'],
    ]
    search = 'DTT'
    result = func(grid, search)
    print(result)
    search = 'UMTTA'
    result = func(grid, search)
    print(result)
    search = 'JAG'
    result = func(grid, search)
    print(result)
