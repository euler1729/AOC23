import re

def lower(time, record):
    l, r = 1, time-1
    res = -1
    while l<=r:
        m = l + (r-l)//2
        if(m*(time-m)>record):
            res = m
            r = m-1
        else:
            l = m+1
    return res

def part1(file):
    with open(file, 'r') as file:
        data = file.read().splitlines()
        time = re.findall(r'(\d+)', data[0])
        time = [int(t) for t in time]
        records = re.findall(r'(\d+)', data[1])
        records = [int(r) for r in records]
        ways = 1
        for i in range(len(time)):
            low = lower(time[i], records[i])
            way = time[i]-low
            way = way - low + 1
            ways = ways * way
        return ways

# print("Part 1: ", part1('d6.txt'))

## Part 2
def part2(file):
    with open(file, 'r') as file:
        data = file.read().splitlines()
        time = re.findall(r'(\d+)', data[0])
        records = re.findall(r'(\d+)', data[1])
        t = ""
        r = ""
        for x in time:
            t += x
        for x in records:
            r += x
        t = int(t)
        r = int(r)
        low = lower(t, r)
        way = t - low
        way = way - low + 1
        return way
print("Part 2: ", part2('d6.txt'))