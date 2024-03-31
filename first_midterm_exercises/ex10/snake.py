from searching_framework import *


def ProdolzhiPravo(snake_body, snake_orientation, red_apples, green_apples):
    head_coordinates = snake_body[-1]
    if snake_orientation == 'down':
        if head_coordinates[1] - 1 >= 0 and (head_coordinates[0], head_coordinates[1] - 1) not in red_apples and (
                head_coordinates[0], head_coordinates[1] - 1) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0], head_coordinates[1] - 1))

            if (head_coordinates[0], head_coordinates[1] - 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
    elif snake_orientation == 'up':
        if head_coordinates[1] + 1 < 10 and (head_coordinates[0], head_coordinates[1] + 1) not in red_apples and (
                head_coordinates[0], head_coordinates[1] + 1) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0], head_coordinates[1] + 1))

            if (head_coordinates[0], head_coordinates[1] + 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)

    elif snake_orientation == 'left':
        if head_coordinates[0] - 1 >= 0 and (head_coordinates[0] - 1, head_coordinates[1]) not in red_apples and (
                head_coordinates[0] - 1, head_coordinates[1]) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0] - 1, head_coordinates[1]))

            if (head_coordinates[0] - 1, head_coordinates[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)

    elif snake_orientation == 'right':
        if head_coordinates[0] + 1 < 10 and (head_coordinates[0] + 1, head_coordinates[1]) not in red_apples and (
                head_coordinates[0] + 1, head_coordinates[1]) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0] + 1, head_coordinates[1]))

            if (head_coordinates[0] + 1, head_coordinates[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)

    return snake_body, snake_orientation, green_apples


def SvrtiDesno(snake_body, snake_orientation, red_apples, green_apples):
    head_coordinates = snake_body[-1]
    if snake_orientation == 'down':
        if head_coordinates[0] - 1 >= 0 and (head_coordinates[0] - 1, head_coordinates[1]) not in red_apples and (
                head_coordinates[0] - 1, head_coordinates[1]) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0] - 1, head_coordinates[1]))

            if (head_coordinates[0] - 1, head_coordinates[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'left'
    elif snake_orientation == 'up':
        if head_coordinates[0] + 1 < 10 and (head_coordinates[0] + 1, head_coordinates[1]) not in red_apples and (
                head_coordinates[0] + 1, head_coordinates[1]) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0] + 1, head_coordinates[1]))

            if (head_coordinates[0] + 1, head_coordinates[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'right'

    elif snake_orientation == 'left':
        if head_coordinates[1] + 1 < 10 and (head_coordinates[0], head_coordinates[1] + 1) not in red_apples and (
                head_coordinates[0], head_coordinates[1] + 1) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0], head_coordinates[1] + 1))

            if (head_coordinates[0], head_coordinates[1] + 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'up'

    elif snake_orientation == 'right':
        if head_coordinates[1] - 1 >= 0 and (head_coordinates[0], head_coordinates[1] - 1) not in red_apples and (
                head_coordinates[0], head_coordinates[1] - 1) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0], head_coordinates[1] - 1))

            if (head_coordinates[0], head_coordinates[1] - 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'down'

    return snake_body, snake_orientation, green_apples


def SvrtiLevo(snake_body, snake_orientation, red_apples, green_apples):
    head_coordinates = snake_body[-1]
    if snake_orientation == 'down':
        if head_coordinates[0] + 1 < 10 and (head_coordinates[0] + 1, head_coordinates[1]) not in red_apples and (
                head_coordinates[0] + 1, head_coordinates[1]) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0] + 1, head_coordinates[1]))

            if (head_coordinates[0] + 1, head_coordinates[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'right'
    elif snake_orientation == 'up':
        if head_coordinates[0] - 1 >= 0 and (head_coordinates[0] - 1, head_coordinates[1]) not in red_apples and (
                head_coordinates[0] - 1, head_coordinates[1]) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0] - 1, head_coordinates[1]))

            if (head_coordinates[0] - 1, head_coordinates[1]) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'left'

    elif snake_orientation == 'left':
        if head_coordinates[1] - 1 >= 0 and (head_coordinates[0], head_coordinates[1] - 1) not in red_apples and (
                head_coordinates[0], head_coordinates[1] - 1) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0], head_coordinates[1] - 1))

            if (head_coordinates[0], head_coordinates[1] - 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'down'

    elif snake_orientation == 'right':
        if head_coordinates[1] + 1 < 10 and (head_coordinates[0], head_coordinates[1] + 1) not in red_apples and (
                head_coordinates[0], head_coordinates[1] + 1) not in snake_body:
            snake_body = list(snake_body)
            snake_body.append((head_coordinates[0], head_coordinates[1] + 1))

            if (head_coordinates[0], head_coordinates[1] + 1) in green_apples:
                green_apples = list(green_apples)
                green_apples = [x for x in green_apples if x not in snake_body]
                green_apples = tuple(green_apples)
            else:
                snake_body = snake_body[1:]
            snake_body = tuple(snake_body)
            snake_orientation = 'up'

    return snake_body, snake_orientation, green_apples


class Snake(Problem):
    def __init__(self, initial, red_apples, goal=None):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    def successor(self, state):
        successors = dict()

        snake_body = state[0]
        orientation = state[1]
        coordinates_green = state[2]

        new_snake_body, new_orientation, new_green_apples = ProdolzhiPravo(snake_body, orientation, self.red_apples,
                                                                           coordinates_green)
        if new_snake_body != snake_body:
            successors['ProdolzhiPravo'] = (new_snake_body, new_orientation, new_green_apples)

        new_snake_body, new_orientation, new_green_apples = SvrtiLevo(snake_body, orientation, self.red_apples,
                                                                      coordinates_green)
        if new_snake_body != snake_body:
            successors['SvrtiLevo'] = (new_snake_body, new_orientation, new_green_apples)

        new_snake_body, new_orientation, new_green_apples = SvrtiDesno(snake_body, orientation, self.red_apples,
                                                                       coordinates_green)
        if new_snake_body != snake_body:
            successors['SvrtiDesno'] = (new_snake_body, new_orientation, new_green_apples)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    num_green = int(input())
    coordinates_green = []
    for i in range(num_green):
        apple = input().split(",")
        apple = [int(apple[0]), int(apple[1])]
        coordinates_green.append(tuple(apple))

    num_red = int(input())
    coordinates_red = []
    for i in range(num_red):
        apple = input().split(",")
        apple = [int(apple[0]), int(apple[1])]
        coordinates_red.append(tuple(apple))

    snake_segments = ((0, 9), (0, 8), (0, 7))
    orientation = 'down'

    snake_problem = Snake((snake_segments, orientation, tuple(coordinates_green)), tuple(coordinates_red))
    snake_problem_solution = breadth_first_graph_search(snake_problem)
    if snake_problem_solution is not None:
        print(snake_problem_solution.solution())
