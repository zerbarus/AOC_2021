from collections import Counter


def task1(lines):
    counter = Counter()
    for line in lines:
        start, end = line.split(" -> ")
        start_x, start_y = map(int, start.split(","))
        end_x, end_y = map(int, end.split(","))

        if start_x == end_x:
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                counter.update([(start_x, y)])
        if start_y == end_y:
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                counter.update([(x, start_y)])
    return len([point for point, occurrences in counter.most_common() if occurrences >= 2])

def task2(lines):
    counter = Counter()
    for line in lines:
        start, end = line.split(" -> ")
        start_x, start_y = map(int, start.split(","))
        end_x, end_y = map(int, end.split(","))
        diff_x = end_x - start_x
        diff_y = end_y - start_y
        if start_x == end_x:
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                counter.update([(start_x, y)])
        if start_y == end_y:
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                counter.update([(x, start_y)])
        if abs(diff_x) == abs(diff_y):
            x, y = start_x, start_y
            while x != end_x and y != end_y:
                counter.update([(x, y)])
                x += 1 if diff_x > 0 else -1
                y += 1 if diff_y > 0 else -1
            counter.update([(end_x, end_y)])
    return len([point for point, occurrences in counter.most_common() if occurrences >= 2])


if __name__ == '__main__':
    with open("day05.txt") as f:
        lines = f.read().splitlines()

        print(task1(lines))
        print(task2(lines))
