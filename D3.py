import re

## Part 1
def isPart(r, c, l, w, h, grid):
    if c-1>=0 and grid[r][c-1] != '.' and (grid[r][c-1].isdigit()==False):
        return True;
    if c+l<w and grid[r][c+l] != '.' and (grid[r][c+l].isdigit()==False):
        return True;
    if r>0:
        i = r-1
        j = max(0, c-1)
        while j<min(w, c+l+1):
            if grid[i][j] != '.' and (grid[i][j].isdigit()==False):
                return True;
            j+=1
    if r+1<h:
        i = r+1
        j = max(0, c-1)
        while j<min(w, c+l+1):
            if grid[i][j] != '.' and (grid[i][j].isdigit()==False):
                return True;
            j+=1
    return False


def power(line):
    sum = 0

    with open(line, 'r') as file:
        grid = [line.strip('\n') for line in file]
        w = len(grid[0])
        h = len(grid)
        for i in range(h):
            row = grid[i]
            cols = re.findall(r'\d+', row)
            k = 0
            for n in cols:
                if n.isnumeric():
                    l = len(n)
                    y = row.find(n, k)
                    k = y + l

                    if isPart(i, y, l, w, h, grid):
                        sum += int(n)
                
    return sum

print("Part 1: ",power('d3.txt'))

## Part 2
def check(r, c, w, h, grid, nums):
    adj = []
    if r-1>=0:
        i = r-1
        s = ''
        j = c-1
        while j>=0 and grid[i][j].isdigit():
            s = grid[i][j] + s
            j-=1
        s = s + grid[i][c]
        j = c+1
        while j<w and grid[i][j].isdigit():
            s = s + grid[i][j]
            j+=1
        for n in re.findall(r'\d+', s):
            adj.append(int(n))
    if r+1<h:
        i = r+1
        s = ''
        j = c-1
        while j>=0 and grid[i][j].isdigit():
            s = grid[i][j] + s
            j-=1
        s = s + grid[i][c]
        j = c+1
        while j<w and grid[i][j].isdigit():
            s = s + grid[i][j]
            j+=1
        for n in re.findall(r'\d+', s):
            adj.append(int(n))
    if c-1>=0 and grid[r][c-1].isdigit():
        s = ''
        j = c-1
        while j>=0 and grid[r][j].isdigit():
            s = grid[r][j] + s
            j-=1
        adj.append(int(s))
    if c+1<w and grid[r][c+1].isdigit():
        s = ''
        j = c+1
        while j<w and grid[r][j].isdigit():
            s = s + grid[r][j]
            j+=1
        adj.append(int(s))
    if len(adj)==2:
        return adj[0]*adj[1]
    return 0

def ratio(line):
    sum = 0

    with open(line, 'r') as file:
        grid = [line.strip('\n') for line in file]
        nums = []
        for g in grid:
            nums .append(re.findall(r'\d+', g))

        w = len(grid[0])
        h = len(grid)

        for i in range(h):
            for j in range(w):
                if grid[i][j]=='*':
                    sum += check(i, j, w, h, grid, nums)
    return sum

print("Part 2: ", ratio('d3.txt'))