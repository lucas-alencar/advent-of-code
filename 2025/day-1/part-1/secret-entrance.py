INITIAL_DIAL_POINT = 50

if __name__ == "__main__":
    current_point = INITIAL_DIAL_POINT
    zero_count = 0
    with open("input.txt") as file:
        for line in file:
            if not (line := line.strip()):
                continue

            direction = line[0]
            distancy = int(line[1:]) % 100

            match direction:
                case 'L':
                    current_point = (current_point - distancy) % 100
                case 'R':
                    current_point = (current_point + distancy) % 100
                case _:
                    raise Exception("Invalid line: " + line)

            if current_point == 0:
                zero_count += 1

    print(zero_count)
