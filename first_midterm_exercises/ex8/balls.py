from searching_framework import *


class Balls(Problem):
    def __init__(self, initial, no_balls, size, goal=None):
        super().__init__(initial)
        self.no_balls = no_balls
        self.size = size
        self.goal = (size // 2, size - 1)

    def successor(self, state):
        successor = {}
        balls = state
        moves = ["Gore Levo:", "Gore Desno:", "Dolu Levo:", "Dolu Desno:", "Levo:", "Desno:"]
        coords1 = [(-2, 2), (2, 2), (-2, -2), (2, -2), (-2, 0), (2, 0)]
        between1 = [(-1, +1), (1, 1), (-1, -1), (1, -1), (-1, 0), (1, 0)]
        for i in range(0, len(balls)):
            for move, coords, between in zip(moves, coords1, between1):
                current_balls = [list(ball) for ball in balls]

                new_ball = (current_balls[i][0] + coords[0], current_balls[i][1] + coords[1])

                if self.is_valid(new_ball):
                    ball_in_between = [current_balls[i][0] + between[0], current_balls[i][1] + between[1]]

                    if ball_in_between in current_balls:
                        x, y = current_balls[i]
                        current_balls[i] = new_ball
                        current_balls = [tuple(ball) for ball in current_balls if ball != ball_in_between]
                        successor[f"{move} (x={x},y={y})"] = tuple(current_balls)

        return successor

    def is_valid(self, node):
        x, y = node
        if x < 0 or x > size or y < 0 or y > size or node in no_balls:
            return False
        return True

    def actions(self, state):
        return self.successor(state)

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state) == 1 and state[0] == self.goal


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
    balls_solution = breadth_first_graph_search(balls_problem)
    if balls_solution is not None:
        print(balls_solution.solution())
