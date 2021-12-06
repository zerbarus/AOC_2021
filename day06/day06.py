from collections import Counter


def simulate(initial, days):
    current_population = initial.copy()
    for day in range(days):
        new_population = {}
        resetted_fish = 0
        new_fish = 0
        for fish_timer in range(9):
            if fish_timer == 0:
                new_fish = resetted_fish = current_population.get(0, 0)
            elif fish_timer == 8:
                new_population[7] = current_population.get(8, 0)
                new_population[8] = new_fish
            elif fish_timer == 7:
                new_population[6] = current_population.get(7, 0) + resetted_fish
            else:
                new_population[fish_timer - 1] = current_population.get(fish_timer, 0)
        current_population = new_population.copy()
    return sum(current_population.values())


def task1(population):
    return simulate(population, 80)


def task2(population):
        return simulate(population, 256)


if __name__ == '__main__':
    with open("day06.txt") as f:
        initial_population = dict(Counter(map(int, f.read().split(","))))
        print(task1(initial_population))
        print(task2(initial_population))
