from searching_framework import Problem, astar_search


def check_validity(human, house, walls, size):
    if human in walls or human[0] < 0 or human[0] >= size or human[1] < 0 or human[1] >= size:
        return False
    return True


def Desno_2(human, house, walls, size):
    new_human = (human[0] + 2, human[1])
    if check_validity(new_human, house, walls, size) is True and (human[0] + 1, human[1]) not in walls:
        return new_human
    return human


def Desno_3(human, house, walls, size):
    new_human = (human[0] + 3, human[1])
    if check_validity(new_human, house, walls, size) is True and (human[0] + 1, human[1]) not in walls and \
            (human[0] + 2, human[1]) not in walls:
        return new_human
    return human


def Gore(human, house, walls, size):
    new_human = (human[0], human[1] + 1)
    if check_validity(new_human, house, walls, size) is True:
        return new_human
    return human


def Dolu(human, house, walls, size):
    new_human = (human[0], human[1] - 1)
    if check_validity(new_human, house, walls, size) is True:
        return new_human
    return human


def Levo(human, house, walls, size):
    new_human = (human[0] - 1, human[1])
    if check_validity(new_human, house, walls, size) is True:
        return new_human
    return human


class maze(Problem):
    def __init__(self, initial, house, walls, size, goal=None):
        super().__init__(initial, goal)
        self.house = house
        self.walls = walls
        self.size = size

    def successor(self, state):
        successors = dict()

        human = state

        new_human = Desno_2(human, self.house, self.walls, self.size)
        if new_human != human:
            successors['Desno 2'] = new_human

        new_human = Desno_3(human, self.house, self.walls, self.size)
        if new_human != human:
            successors['Desno 3'] = new_human

        new_human = Dolu(human, self.house, self.walls, self.size)
        if new_human != human:
            successors['Dolu'] = new_human

        new_human = Levo(human, self.house, self.walls, self.size)
        if new_human != human:
            successors['Levo'] = new_human

        new_human = Gore(human, self.house, self.walls, self.size)
        if new_human != human:
            successors['Gore'] = new_human

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.house

    def h(self, node):
        x1, y1 = node.state
        x2, y2 = self.house
        return (abs(x2 - x1) + abs(y2 - y1)) / 3


if __name__ == '__main__':
    size = int(input())
    number_walls = int(input())
    walls_coordinates = tuple(tuple(map(int, input().split(","))) for _ in range(number_walls))
    human = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    initial = tuple(human)

    maze_problem = maze(initial, house, walls_coordinates, size)
    maze_solution = astar_search(maze_problem)

    if maze_solution is not None:
        print(maze_solution.solution())
    else:
        print("No solution found")
