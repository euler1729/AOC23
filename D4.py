import re
## Part  1
def points(file):
    with open(file, 'r') as file:
        p = 0
        while True:
            line = file.readline().strip('\n')
            if not line:
                break
            line = line.split(": ")[1]
            win, cards = line.split(' | ')
            win = re.findall(r'\d+', win)
            cards = re.findall(r'\d+', cards)
            cnt = len(set(win).intersection(set(cards)))
            if cnt>0:
                p += 2**(cnt-1)
    return p
# print("Part 1: ",points("d4.txt"))

## Part 2
def count(file):
    with open(file, 'r') as file:
        win_count = []
        while True:
            line = file.readline().strip('\n')
            if not line:
                break
            line = line.split(": ")[1]
            win, cards = line.split(' | ')
            win = re.findall(r'\d+', win)
            cards = re.findall(r'\d+', cards)
            cnt = len(set(win).intersection(set(cards)))
            win_count.append(cnt)
        n = len(win_count)
        instances = [1]*n
        total = 0
        for i in range(n):
            total += instances[i]
            for j in range(i+1, i+win_count[i]+1, 1):
                instances[j] += instances[i]
        return total
print("Part 2: ", count('d4.txt'))
