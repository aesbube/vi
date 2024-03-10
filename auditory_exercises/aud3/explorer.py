from searching_framework import Problem, breadth_first_graph_search


class Explorer(Problem):
    def __init__(self, person, house):
        super().__init__((person, (2, 5, -1), (5, 0, +1)))
        self.house = house
        self.rows = 6
        self.cols = 8

    def goal_test(self, state):
        person = state[0]
        return person == self.house

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        neighbors = dict()

        actions = ("up", "down", "left", "right")
        directions = ((+1, 0), (-1, 0), (0, +1), (0, -1))

        for action, direction in zip(actions, directions):
            res = self.move(state, direction)
            if res is not None: neighbors[action] = res

        return neighbors

    def move(self, state, direction):
        person = self.move_person(state[0], direction)
        block1 = self.move_block(state[1])
        block2 = self.move_block(state[2])

        new_state = (person, block1, block2)

        if self.is_valid(new_state):
            return new_state
        else:
            return None

    def move_person(self, person, direction):
        person = list(person)
        person[0] += direction[0]
        person[1] += direction[1]
        return tuple(person)

    def move_block(self, block):
        dir_x, dir_y, n = block
        dir_y += n
        if dir_y < 0 or dir_y >= self.rows:
            n *= -1
            dir_y += 2 * n
        return (dir_x, dir_y, n)

    def is_valid(self, state):
        person, block1, block2 = state
        dir_x, dir_y = person
        return 0 <= dir_x < self.cols and \
            0 <= dir_y < self.rows and \
            person != block1[:2] and person != block2[:2]


if __name__ == '__main__':
    person = tuple(map(int, input().split()))
    house = tuple(map(int, input().split()))
    problem = Explorer(person, house)
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
    else:
        print("Cannot be solved")
