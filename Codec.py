def direction(input1, input2):
    x = 1
    y = 1
    direction = 'N'

    rows = int(input1[0])
    columns = int(input1[2])
    F = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}

    for i in input2:
        if i == 'F':
            x += F[direction][0]
            x = min(rows, max(1, x))
            y += F[direction][1]
            y = min(columns, max(1, y))
        else:
            if direction == 'N':
                direction = 'E' if i == 'R' else 'W'
            elif direction == 'S':
                direction = 'W' if i == 'R' else 'E'
            elif direction == 'W':
                direction = 'N' if i == 'R' else 'S'
            else:
                direction = 'S' if i == 'R' else 'N'

    print(f"{x}, {y}, {direction}")
    return x, y, direction
