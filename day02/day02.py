def task1():
    horizontal_pos = 0
    depth = 0
    for line in lines:
        match line.split():
            case ['forward', distance]:
                horizontal_pos += int(distance)
            case ['down', distance]:
                depth += int(distance)
            case ['up', distance]:
                depth -= int(distance)
            case _:
                pass
    return horizontal_pos * depth


def task2():
    horizontal_pos = 0
    depth = 0
    aim = 0
    for line in lines:
        match line.split():
            case ['forward', distance]:
                horizontal_pos += int(distance)
                depth += aim * int(distance)
            case ['down', distance]:
                aim += int(distance)
            case ['up', distance]:
                aim -= int(distance)
            case _:
                pass
    return horizontal_pos * depth


if __name__ == '__main__':
    with open("day02-test.txt") as f:
        lines = f.read().splitlines()
        print(task1())
        print(task2())
