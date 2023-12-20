file = open('If You Give A Seed A Fertiliser.in')
converters = {}
current_converter = ''
seeds1 = []
seeds2 = []
locations1 = []
locations2 = []

def converting(inp, converter):
    for r in converters[converter]:
        if inp in range(r[0], r[1]):
            return inp + converters[converter][r]
    return inp

for line in file:
    if line == '\n':
        continue
    try:
        parts = list(map(int, line.split()))
    except ValueError:
        parts = line.split()
        if parts[0] == 'seeds:':
            seeds1 = list(map(int, parts[1:]))
            for n in range(1, len(parts), 2):
                seeds2.append([int(parts[n]), int(parts[n]) + int(parts[n+1])])
        else:
            current_converter = parts[0]
            converters[parts[0]] = {}
        continue
    converters[current_converter][parts[1], parts[1] + parts[2]] = parts[0] - parts[1]
for seed in seeds1:
    i = seed
    for converter in converters:
        i = converting(i, converter)
    locations1 += [i]
for converter in converters:
    current_values = []
    while len(seeds2) > 2:
        [start, end] = seeds2.pop()
        for s, e in converters[converter]:
            shift_s = max(start, s)
            shift_e = min(end, e)
            if shift_s < shift_e:
                current_values.append([shift_s + converters[converter][(s, e)], shift_e + converters[converter][(s, e)]])
                if shift_s > start:
                    seeds2.append([start, shift_s])
                if end > shift_e:
                    seeds2.append([shift_e, end])
                break
        else:
            current_values.append([start, end])
    seeds2 = current_values
print('Part 1:', min(locations1), '\nPart 2:', min(min(current_values)))
