import re
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
            # print(cols)
            k = 0
            for n in cols:
                if n.isnumeric():
                    l = len(n)
                    y = row.find(n, k)
                    k = y + l

                    # print(n, i, y, l)
                    if isPart(i, y, l, w, h, grid):
                        sum += int(n)
                        # print('->',n, i, y)
                
    return sum

print(power('d3.txt'))