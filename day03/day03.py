def most_least(bit_lines: list[str]) -> tuple[str, str]:
    num_lines = len(bit_lines)

    # Convert ['1011', '1101'] to [[1, 0, 1, 1], [1, 1, 0, 1]]
    bits = list(map(lambda line: list(map(int, list(line))), bit_lines))

    # Group all bits at a certain position, i.e. [[1, 0, 1, 1], [1, 1, 0, 1]] to [[1, 1], [0, 1], [1, 0], [1, 1]]
    order_bits = list(zip(*bits))
    bits_sums = list(map(sum, order_bits))

    # If the sum of 0s and 1s is not even half as much as the number of bits, there are more 0s
    most_bits_raw = "".join(map(lambda bit_sum: "0" if bit_sum < num_lines / 2 else "1", bits_sums))
    least_bits_raw = "".join(map(lambda most_bit: "1" if most_bit == "0" else "0", most_bits_raw))
    return most_bits_raw, least_bits_raw


def filter_by_bit_mask(lines: list[str], use_most=True) -> int:
    filtered = lines.copy()
    for bit_position in range(len(lines)):
        most_bits_raw, least_bits_raw = most_least(filtered)
        bit_mask = most_bits_raw if use_most else least_bits_raw
        filtered = list(filter(lambda x: x[bit_position] == bit_mask[bit_position], filtered))
        if len(filtered) == 1:
            return int(filtered[0], 2)


def task1(lines: list[str]) -> int:
    most_bits_raw, least_bits_raw = most_least(lines)

    gamma = int(most_bits_raw, 2)
    epsilon = int(least_bits_raw, 2)
    return gamma * epsilon


def task2(lines: list[str]) -> int:
    o2 = filter_by_bit_mask(lines)
    co2 = filter_by_bit_mask(lines, use_most=False)
    return o2 * co2


if __name__ == '__main__':
    with open("day03-test.txt") as f:
        lines = f.read().splitlines()
        print(task1(lines))
        print(task2(lines))
