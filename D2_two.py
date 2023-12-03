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

print(power('d2.txt'))