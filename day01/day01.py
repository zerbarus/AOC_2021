def count_diffs(data: list[int]) -> int:
    """Count all times a next depth measurement is less than the previous one"""
    return sum([x < y for x, y in zip(data, data[1:])])


if __name__ == '__main__':
    with open("day01-test.txt") as f:
        lines = f.read().splitlines()

        # tasks 1
        depths = list(map(int, lines))
        print(count_diffs(depths))

        # task 2
        # Create windows of 3 depth measures
        windows = [sum(depths[i:i+3]) for i in range(len(depths))]
        print(count_diffs(windows))
