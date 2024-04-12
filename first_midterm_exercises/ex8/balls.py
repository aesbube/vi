from searching_framework import *


class Balls(Problem):
    def __init__(self, initial, no_balls, size, goal=None):
        super().__init__(initial, goal)
        self.no_balls = no_balls
        self.size = size
        self.moves = {
            'GoreLevo': (-2, 2),
            'GoreDesno': (2, 2),
            'DoluLevo': (-2, -2),
            'DoluDesno': (2, -2),
            'Levo': (-2, 0),
            'Desno': (2, 0)
        }

    def successor(self, state):
        succ = {}

        return succ

    @staticmethod
    def is_valid(node):
        x, y = node
        if x < 0 or x > size or y < 0 or y > size:
            return False
        
        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state) == 1 and state[0][0] == self.size / 2 - 1 and state[0][1] == self.size - 1


# balls 😔
if __name__ == '__main__':
    size = int(input())
    num_of_balls = int(input())
    balls = tuple()
    for _ in range(num_of_balls):
        balls += (tuple(map(int, input().split(','))),)

    num_of_no_balls = int(input())
    no_balls = tuple()
    for _ in range(num_of_no_balls):
        no_balls += (tuple(map(int, input().split(','))),)

    balls_problem = Balls(balls, no_balls, size)
    balls_solution = breadth_first_graph_search(balls_problem).solution()
    if balls_solution is not None:
        print(balls_solution)
