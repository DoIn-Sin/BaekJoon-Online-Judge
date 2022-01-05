count = 0
place = []
for line in range(8):
    place.append(list(input()))

for row in range(8):
    for column in range(8):
        if (row + column) % 2 == 0:
            if place[row][column] == 'F':
                count += 1
print(count)