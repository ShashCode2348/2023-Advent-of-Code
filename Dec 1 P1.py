total_p1 = total_p2 = 0
line_digits_p1 = line_digits_p2 = ''
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
with open("Trebuchet.in") as file:
    for line in file:
        for pos, char in enumerate(line):
            if char in '0123456789':
                line_digits_p1 += char
                line_digits_p2 += char
            word_num = list(digit for digit, number in enumerate(numbers, 1) if line[pos:].startswith(number))
            if word_num != []:
                line_digits_p2 += str(word_num[0])       
        total_p1 += int(f'{line_digits_p1[0]}{line_digits_p1[len(line_digits_p1)-1]}')
        total_p2 += int(f'{line_digits_p2[0]}{line_digits_p2[len(line_digits_p2)-1]}')
        line_digits_p1 = line_digits_p2 = ''
print(f'Part 1:{total_p1}\nPart 2:{total_p2}')
