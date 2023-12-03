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

print(possible('d2.txt'))