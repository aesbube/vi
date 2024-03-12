from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial)
        self.red_apples = red_apples
        self.matrix_size = 10
        self.actions = ('ProdolzhiPravo', 'SvrtiDesno', 'SvrtiLevo')
        self.directions = {'ProdolzhiPravo': 0, 'SvrtiDesno': 1, 'SvrtiLevo': -1}
        self.moves = ((0, -1), (+1, 0), (0, +1), (-1, 0))

    def successor(self, state):
        next_moves = {}

        for action in self.actions:
            next_move =

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):
        pass


    def make_a_move(self, state, action):
        direction = (state[1] + self.directions[action])
        move = self.moves[direction]
        head =
