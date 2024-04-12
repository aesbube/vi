from searching_framework import Problem, breadth_first_graph_search


# poveli nepederski reshena zadacha (slavam bakiiiiiii)

class Squares(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        self.moves = {
            'gore': (0, 1),
            'dolu': (0, -1),
            'levo': (-1, 0),
            'desno': (1, 0)
        }

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state):
        x, y = state
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        return True

    def successor(self, state):
        succ = {}
        for i, square in enumerate(state):
            for move in self.moves.keys():
                new_square = (square[0] + self.moves[move][0], square[1] + self.moves[move][1])

                if self.check_valid(new_square) is False:
                    continue

                succ[f'Pomesti kvadratche {i + 1} {move}'] = self.generate_state(state, i, new_square)

        return succ

    def generate_state(self, state, index, new_square):
        new_state = []

        for i, square in enumerate(state):
            if i == index:
                new_state.append(new_square)
            else:
                new_state.append(square)

        return tuple(new_state)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))),)

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)
    problem = breadth_first_graph_search(squares).solution()

    if problem is not None:
        print(problem)
