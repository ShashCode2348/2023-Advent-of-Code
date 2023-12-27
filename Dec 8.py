from math import lcm
file = open('Haunted Wasteland.in')
pattern = ''
nodes = {}
p1 = 0
p2 = 1
current_node = 'AAA'
for line in file:
    if len(line) < 2:
        continue
    if line.count(' ') == 0:
        pattern = [0 if i == 'L' else 1 for i in line][:-1]
        continue
    parts = line.split()
    nodes[parts[0]] = (parts[2][1:-1], parts[3][:-1])
while current_node != 'ZZZ':
    current_node = nodes[current_node][pattern[p1 % len(pattern)]]
    p1 += 1
current_nodes = [node for node in nodes if node[-1] == 'A']
p2_counter = 0
for n in range(len(current_nodes)):
    p2_counter = 0
    while current_nodes[n][-1] != 'Z':
        current_nodes[n] = nodes[current_nodes[n]][pattern[p2_counter % len(pattern)]]
        p2_counter += 1
    p2 = lcm(p2, p2_counter)
print('Part 1:', p1, '\nPart 2:', p2)
