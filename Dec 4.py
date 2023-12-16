import time
start_time = time.time()
import re
p1 = 0
p2 = [1] * sum(1 for _ in open('Scratchcards.in'))
with open('Scratchcards.in') as file:
    for n, line in enumerate(file):
        line_list = list(map(lambda x: x.split(), re.split('[:|]', line)))
        del line_list[0]
        win_nums = list(map(lambda x: x in line_list[1], line_list[0])).count(True)
        if win_nums != 0:
            p1 += 2**(win_nums-1)
        for card in range(n, n+win_nums):
            try:
                p2[card] += p2[n-1]
            except IndexError:
                pass
print('Part 1:', p1, '\nPart 2:', sum(p2))
print("--- %s seconds ---" % (time.time() - start_time))
