from searching_framework import Problem, astar_search


def check_validity(human, house, trees):
    if human not in trees and human != house or human[0] < 0 or human[0] > 4 or human[1] < 0 or human[1] > 8 or \
            house[0] < 0 or house[0] > 4 or house[1] < 0 or house[1] > 8:
        return False
    return True


def Stoj(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    if check_validity(human, new_house, trees) is True:
        return human, new_house, house_dir
    return human, house, house_dir


def Gore_1(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    new_human = (human[0], human[1] + 1)
    if check_validity(new_human, new_house, trees) is True:
        return new_human, new_house, house_dir
    return human, house, house_dir


def Gore_2(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    new_human = (human[0], human[1] + 2)
    if check_validity(new_human, new_house, trees) is True:
        return new_human, new_house, house_dir
    return human, house, house_dir


def Gore_desno_1(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    new_human = (human[0] + 1, human[1] + 1)
    if check_validity(new_human, new_house, trees) is True:
        return new_human, new_house, house_dir
    return human, house, house_dir


def Gore_desno_2(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    new_human = (human[0] + 2, human[1] + 2)
    if check_validity(new_human, new_house, trees) is True:
        return new_human, new_house, house_dir
    return human, house, house_dir


def Gore_levo_1(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    new_human = (human[0] - 1, human[1] + 1)
    if check_validity(new_human, new_house, trees) is True:
        return new_human, new_house, house_dir
    return human, house, house_dir


def Gore_levo_2(human, house, house_dir, trees):
    if house[0] == 0 or house[0] == 4:
        house_dir *= -1
    new_house = (house[0] + house_dir, house[1])
    new_human = (human[0] - 2, human[1] + 2)
    if check_validity(new_human, new_house, trees) is True:
        return new_human, new_house, house_dir
    return human, house, house_dir


class reach_home(Problem):
    def __init__(self, initial, trees, goal=None):
        super().__init__(initial, goal)
        self.trees = trees

    def successor(self, state):
        successors = dict()

        human = state[0]
        house = state[1]
        house_direction = state[2]

        new_human, new_house, new_house_dir = Stoj(human, house, house_direction, self.trees)
        if new_house != house:
            successors['Stoj'] = (new_human, new_house, new_house_dir)

        new_human, new_house, new_house_dir = Gore_1(human, house, house_direction, self.trees)
        if new_house != house and new_human != human:
            successors['Gore 1'] = (new_human, new_house, new_house_dir)

        new_human, new_house, new_house_dir = Gore_2(human, house, house_direction, self.trees)
        if new_house != house and new_human != human:
            successors['Gore 2'] = (new_human, new_house, new_house_dir)

        new_human, new_house, new_house_dir = Gore_desno_1(human, house, house_direction, self.trees)
        if new_house != house and new_human != human:
            successors['Gore-desno 1'] = (new_human, new_house, new_house_dir)

        new_human, new_house, new_house_dir = Gore_desno_2(human, house, house_direction, self.trees)
        if new_house != house and new_human != human:
            successors['Gore-desno 2'] = (new_human, new_house, new_house_dir)

        new_human, new_house, new_house_dir = Gore_levo_1(human, house, house_direction, self.trees)
        if new_house != house and new_human != human:
            successors['Gore-levo 1'] = (new_human, new_house, new_house_dir)

        new_human, new_house, new_house_dir = Gore_levo_2(human, house, house_direction, self.trees)
        if new_house != house and new_human != human:
            successors['Gore-levo 2'] = (new_human, new_house, new_house_dir)

        return successors

    def h(self, node):
        return (8 - node.state[0][1]) / 2

    def goal_test(self, state):
        return state[0] == state[1]

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    human_coordinates = tuple(map(int, input().split(",")))
    house_coordinates = tuple(map(int, input().split(",")))
    house_direction = input()
    house_dir = -1
    if house_direction == "desno":
        house_dir *= -1
    trees_coordinates = ((1, 0), (2, 0), (3, 0),
                         (1, 1), (2, 1),
                         (0, 2), (2, 2), (4, 2),
                         (1, 3), (3, 3), (4, 3),
                         (0, 4), (2, 4),
                         (2, 5), (3, 5),
                         (0, 6), (2, 6),
                         (1, 7), (3, 7))
    initial = (human_coordinates, house_coordinates, house_dir)
    reach_home_problem = reach_home(initial, trees_coordinates)
    reach_home_solution = astar_search(reach_home_problem)

    if reach_home_solution is not None:
        print(reach_home_solution.solution())
    else:
        print("No solution found")
