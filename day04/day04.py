from collections import defaultdict


class Board:
    def __init__(self, board_rows: list[str]):
        self.rows = defaultdict(int)
        self.cols = defaultdict(int)
        self.numbers = {}

        for row_idx, row in enumerate(board_rows):
            for col_idx, value in enumerate(row.split()):
                self.numbers[int(value)] = (row_idx, col_idx)
        assert len(self.numbers.keys()) == 25

    def mark(self, number: int) -> bool:
        if self.numbers.get(number):
            row_idx, col_idx = self.numbers[number]
            self.rows[row_idx] += 1
            self.cols[col_idx] += 1
            del self.numbers[number]
            return self.check_win()

    def check_win(self) -> bool:
        return bool(list(filter(lambda x: x >= 5, self.rows.values())) or list(filter(lambda x: x >= 5, self.cols.values())))

    def sum_left_numbers(self) -> int:
        return sum(self.numbers.keys())


def task1(draws, boards):
    for draw in draws:
        for board in boards:
            if board.mark(draw):
                return draw * board.sum_left_numbers()


def task2(draws, boards):
    for draw in draws:
        boards_to_delete = []
        for board_idx, board in enumerate(boards):
            if board.mark(draw):
                boards_to_delete.append(board)

        for delete_board in boards_to_delete:
            boards.remove(delete_board)
            score = draw * board.sum_left_numbers()
            if len(boards) == 0:
                return score


def parse_boards(board_lines: list[str]) -> list[Board]:
    boards = []
    num_boards = len(board_lines) // 6

    for i in range(num_boards):
        boards.append(Board(board_lines[(i*6)+1:(i+1)*6]))
    return boards

if __name__ == '__main__':
    with open("day04-test.txt") as f:
        lines = f.read().splitlines()
        draws = list(map(int, lines[0].split(",")))
        boards = parse_boards(lines[1:])
        print(task1(draws, boards))
        print(task2(draws, boards))