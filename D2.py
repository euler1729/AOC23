## Part 1
def possible(line):
    sum = 0

    cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    with open(line, 'r') as file:
        for line in file:
            line = line.strip('\n')
            ln = line.split(': ')
            id = ln[0].split(' ')[1]
            sets = ln[1].split('; ')
            isPossible = True
            for s in sets:
                s = s.split(', ')
                for c in s:
                    cc = c.split(' ')
                    if(cubes.get(cc[1])<int(cc[0])):
                        isPossible = False
                        break
                if(not isPossible):
                    break
            if(isPossible):
                sum+=int(id)
    return sum
print("Part 1: ",possible('d2.txt'))

## Part 2
def power(line):
    sum = 0

    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    with open(line, 'r') as file:
        for line in file:
            cnt = cubes.copy()
            line = line.strip('\n')
            ln = line.split(': ')
            # id = ln[0].split(' ')[1]
            sets = ln[1].split('; ')
            for s in sets:
                s = s.split(', ')
                for c in s:
                    cc = c.split(' ')
                    cnt[cc[1]] = max(cnt.get(cc[1]), int(cc[0]))
            sum+=cnt['red']*cnt['green']*cnt['blue']
    return sum
print("Part 2: ",power('d2.txt'))