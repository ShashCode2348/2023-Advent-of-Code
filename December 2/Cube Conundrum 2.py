max_colours = {'red':0, 'green':0, 'blue':0}
sum_id = 0
sum_powers = 0
with open('Cube Conundrum.in') as file:
    for line in file:
        words = [x.strip(',;:') for x in line.split()]
        for n, word in enumerate(words):
            try:
                if max_colours[word] < int(words[n-1]):
                    max_colours[word] = int(words[n-1])
            except KeyError:
                pass
        if max_colours['red'] < 13 and max_colours['green'] < 14 and max_colours['blue'] < 15:
            sum_id += int(words[1])
        sum_powers += (max_colours['red'] * max_colours['green'] * max_colours['blue'])
        max_colours = {'red':0, 'green':0, 'blue':0}
print('Part 1: ', sum_id, '\nPart 2: ', sum_powers)
