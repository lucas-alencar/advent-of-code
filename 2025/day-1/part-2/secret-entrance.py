INITIAL_DIAL_POINT = 50

dial_direction = {
    "L": -1,
    "R": 1
}

if __name__ == "__main__":
    current_point = INITIAL_DIAL_POINT
    zero_count = 0

    with open("input.txt") as file:
        for line in file:
            if not (line := line.strip()):
                continue

            direction = line[0]
            full_turns, steps = divmod(int(line[1:]), 100)

            zero_count += full_turns

            for _ in range(steps):
                current_point += dial_direction[direction]
                if current_point == 0:
                    zero_count += 1

                if (current_point == -1):
                    current_point = 99

                if (current_point == 100):
                    current_point = 0
                    zero_count += 1


    print(zero_count)
