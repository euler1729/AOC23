import re
import time

## Part  1
class Node:
    def __init__(self, val) -> None:
        self.id = val
        self.next = val

def is_line_numbers(line):
    tokens = line.split()
    for token in tokens:
        if not token.isdigit():
            return False
    return True

def part1(file):
    with open(file, 'r') as file:
        data = file.read().splitlines()
        seeds = re.findall(r'(\d+)', data[0])

        nodes = [Node(int(val)) for val in seeds]

        for item in data[2:]:
            if item=="":
                continue
            if is_line_numbers(item):
                v, u, c = item.split(' ')
                v, u, c = int(v), int(u), int(c)
                for node in nodes:
                        if node.id>=u and node.id<u+c:
                            node.next = v + (node.id-u)
            else:
                for node in nodes:
                    node.id = node.next
        mn = 99999999999999999
        for node in nodes:
            mn = min(mn, node.next)
    return mn
         
print("Part 1: ",part1("d5.txt"))

## Part 2
class Node2:
    def __init__(self, id, r) -> None:
        self.id = id;
        self.next = id;
        self.r = r

def part2(file):
    with open(file, 'r') as file:
        data = file.read().splitlines()
        seeds = re.findall(r'(\d+)', data[0])
        nodes = []

        for i in range(0, len(seeds), 2):
            nodes.append(Node2(int(seeds[i]), int(seeds[i+1])))

        for item in data[2:]:
            if item=="":
                continue
            if is_line_numbers(item):
                v, u, c = item.split(' ')
                v, u, c = int(v), int(u), int(c)
                i = 0
                length = len(nodes)
                tmp = []
                while(i<length):
                    node = nodes[i];
                    start = max(node.id, u);
                    end = min(node.id+node.r-1, u+c-1)
                    if start<=end: ## current segment overlaps
                        nodes.pop(i)
                        node_left = start-node.id
                        node_right = (node.id+node.r-1)-end

                        if node_left>0: ## left segment that doesn't overlap
                            tmp.append(Node2(node.id, node_left))

                        if node_right>0: ## right segment that doesn't overlap
                            tmp.append(Node2(end+1, node_right))

                        newnode = Node2(start, end-start+1) ##segment that overlaps
                        newnode.next = v + abs(u-start) ## maps to next layer
                        tmp.append(newnode)
                        length -= 1
                    else:
                        i = i + 1
                for t in tmp:
                    nodes.append(t)
            else:
                for node in nodes:
                    node.id = node.next
        
        mn = 9999999999999999
        for node in nodes:
            mn = min(mn, node.next)
        return mn
    
start_time = time.time()
print("Part 2: ",part2("d5.txt"))
print(time.time()-start_time)