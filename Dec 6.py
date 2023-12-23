from math import sqrt, ceil
file = list(map(lambda x: x.split()[1:], open('Wait For It.in').read().splitlines()))
records = list(map(lambda x, y: (int(x), int(y)), file[0], file[1]))
p1 = 1
for time, distance in records:
    p1 *= int((time + sqrt(time**2 - 4*distance))/2) - ceil((time - sqrt(time**2 - 4*distance))/2) + 1
time = int(''.join(map(lambda x:str(x[0]), records)))
distance = int(''.join(map(lambda x:str(x[1]), records)))
p2 = int((time + sqrt(time**2 - 4*distance))/2) - ceil((time - sqrt(time**2 - 4*distance))/2) + 1
print('Part 1:', p1, '\nPart 2:', p2)
