import re
raw_file = open('Gear Ratios.in').read().splitlines()
special_chars = '&+-#@$*/%='
char_index = 1
raw_file.insert(0, '.'*len(raw_file[0]))
raw_file.append('.'*len(raw_file[0]))
file = ['.' + line + '.' for line in raw_file]
temp_store = ['', False, [None, None]]    #store of digits, number to be added once complete, Gear ID to be added to
p1 = 0
gear_id = {}
for n, line in enumerate(file[1:-1], start=1):
    for char_index, char in enumerate(line[1:-1], start=1):
        if char not in '0123456789' or char_index == 1:
            if temp_store[0] != '':
                if temp_store[1] == True:
                    p1 += int(temp_store[0])
                if temp_store[2] != [None, None]:
                    try:
                        gear_id[tuple(temp_store[2])][0] *= int(temp_store[0])
                        gear_id[tuple(temp_store[2])][1] += 1
                    except:
                        gear_id[tuple(temp_store[2])] = [int(temp_store[0]), 1]
                temp_store = ['', False, [None, None]]
        if char not in '0123456789':
            continue
        adjacent_chars = {file[n-1][char_index-1]:[n-1, char_index-1], file[n-1][char_index]:[n-1, char_index], file[n-1][char_index+1]:[n-1, char_index+1],
                          file[n][char_index-1]:[n, char_index-1], file[n][char_index+1]:[n, char_index+1],
                          file[n+1][char_index-1]:[n+1, char_index-1], file[n+1][char_index]:[n+1, char_index], file[n+1][char_index+1]:[n+1, char_index+1]}
        temp_store[0] += char
        if any(map(lambda x: x in special_chars, list(adjacent_chars.keys()))):
            temp_store[1] = True
        if '*' in list(adjacent_chars.keys()):
            temp_store[2] = adjacent_chars['*']
print('Part 1: ', p1, '\nPart 2: ', sum([x[0] for x in gear_id.values() if x[1] == 2]))
