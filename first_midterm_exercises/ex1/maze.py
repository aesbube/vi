from searching_framework import *


def check_valid(ghost, walls, size):
    if ghost[0] < 0 or ghost[1] < 0 or ghost[0] > size or ghost[1] > size or ghost in walls:
        return False
    return True


def Up_1(ghost, walls, size):
    new_ghost = (ghost[0], ghost[1] + 1)
    if check_valid(new_ghost, walls, size) is True:
        return new_ghost
    return ghost


def Up_2(ghost, walls, size):
    new_ghost = (ghost[0], ghost[1] + 2)
    if check_valid(new_ghost, walls, size) is True:
        return new_ghost
    return ghost


def Up_3(ghost, walls, size):
    new_ghost = (ghost[0], ghost[1] + 3)
    if check_valid(new_ghost, walls, size) is True:
        return new_ghost
    return ghost


def Right_1(ghost, walls, size):
    new_ghost = (ghost[0] + 1, ghost[1])
    if check_valid(new_ghost, walls, size) is True:
        return new_ghost
    return ghost


def Right_2(ghost, walls, size):
    new_ghost = (ghost[0] + 2, ghost[1])
    if check_valid(new_ghost, walls, size) is True:
        return new_ghost
    return ghost


def Right_3(ghost, walls, size):
    new_ghost = (ghost[0] + 3, ghost[1])
    if check_valid(new_ghost, walls, size) is True:
        return new_ghost
    return ghost


class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def successor(self, state):
        successors = dict()

        new_ghost = Up_3(state, self.walls, self.n)
        if new_ghost != state:
            successors['Gore 3'] = new_ghost

        new_ghost = Up_2(state, self.walls, self.n)
        if new_ghost != state:
            successors['Gore 2'] = new_ghost

        new_ghost = Up_1(state, self.walls, self.n)
        if new_ghost != state:
            successors['Gore'] = new_ghost

        new_ghost = Right_3(state, self.walls, self.n)
        if new_ghost != state:
            successors['Desno 3'] = new_ghost

        new_ghost = Right_2(state, self.walls, self.n)
        if new_ghost != state:
            successors['Desno 2'] = new_ghost

        new_ghost = Right_1(state, self.walls, self.n)
        if new_ghost != state:
            successors['Desno'] = new_ghost

        return successors

    def h(self, node):
        return (abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])) / 3
        # return abs(self.n - node.state[1]) / 10


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)
    problem_solution = astar_search(problem)
    if problem_solution is not None:
        print(problem_solution.solution())
