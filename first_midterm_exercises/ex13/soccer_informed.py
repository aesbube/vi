from searching_framework import *


def check_validity(player, ball, enemy_territory):
    if 0 <= player[0] < 8 and 0 <= player[1] < 6 and 0 <= ball[0] < 8 and 0 <= ball[1] < 6 and \
            ball not in enemy_territory and player != ball and player != (3, 3) and player != (5, 4):
        return True
    else:
        return False


def chovecheGore(player, ball, enemy_territory):
    new_player = (player[0], player[1] + 1)
    if check_validity(new_player, ball, enemy_territory) is True:
        return tuple(new_player)
    return tuple(player)


def topkaGore(player, ball, enemy_territory):
    new_ball = (ball[0], ball[1] + 1)
    new_player = (player[0], player[1] + 1)
    if check_validity(new_player, new_ball, enemy_territory) is True and new_player == ball:
        return tuple(new_player), tuple(new_ball)
    return tuple(player), tuple(ball)


def chovecheDolu(player, ball, enemy_territory):
    new_player = (player[0], player[1] - 1)
    if check_validity(new_player, ball, enemy_territory) is True:
        return tuple(new_player)
    return tuple(player)


def topkaDolu(player, ball, enemy_territory):
    new_ball = (ball[0], ball[1] - 1)
    new_player = (player[0], player[1] - 1)
    if check_validity(new_player, new_ball, enemy_territory) is True and new_player == ball:
        return tuple(new_player), tuple(new_ball)
    return tuple(player), tuple(ball)


def chovecheDesno(player, ball, enemy_territory):
    new_player = (player[0] + 1, player[1])
    if check_validity(new_player, ball, enemy_territory) is True:
        return tuple(new_player)
    return tuple(player)


def topkaDesno(player, ball, enemy_territory):
    new_ball = (ball[0] + 1, ball[1])
    new_player = (player[0] + 1, player[1])
    if check_validity(new_player, new_ball, enemy_territory) is True and new_player == ball:
        return tuple(new_player), tuple(new_ball)
    return tuple(player), tuple(ball)


def chovecheGoreDesno(player, ball, enemy_territory):
    new_player = (player[0] + 1, player[1] + 1)
    if check_validity(new_player, ball, enemy_territory) is True:
        return tuple(new_player)
    return tuple(player)


def topkaGoreDesno(player, ball, enemy_territory):
    new_ball = (ball[0] + 1, ball[1] + 1)
    new_player = (player[0] + 1, player[1] + 1)
    if check_validity(new_player, new_ball, enemy_territory) is True and new_player == ball:
        return tuple(new_player), tuple(new_ball)
    return tuple(player), tuple(ball)


def chovecheDoluDesno(player, ball, enemy_territory):
    new_player = (player[0] + 1, player[1] - 1)
    if check_validity(new_player, ball, enemy_territory) is True:
        return tuple(new_player)
    return tuple(player)


def topkaDoluDesno(player, ball, enemy_territory):
    new_ball = (ball[0] + 1, ball[1] - 1)
    new_player = (player[0] + 1, player[1] - 1)
    if check_validity(new_player, new_ball, enemy_territory) is True and new_player == ball:
        return tuple(new_player), tuple(new_ball)
    return tuple(player), tuple(ball)


class Goal(Problem):
    def __init__(self, enemy_territory, goal_coordinates, initial, goal=None):
        super().__init__(initial, goal)
        self.enemy_territory = enemy_territory
        self.goal_coordinates = goal_coordinates

    def successor(self, state):
        successors = dict()
        player = state[0]
        ball = state[1]

        new_player = chovecheGore(player, ball, self.enemy_territory)
        if new_player != player:
            successors['Pomesti coveche gore'] = (new_player, ball)

        new_player = chovecheDolu(player, ball, self.enemy_territory)
        if new_player != player:
            successors['Pomesti coveche dolu'] = (new_player, ball)

        new_player = chovecheDesno(player, ball, self.enemy_territory)
        if new_player != player:
            successors['Pomesti coveche desno'] = (new_player, ball)

        new_player = chovecheGoreDesno(player, ball, self.enemy_territory)
        if new_player != player:
            successors['Pomesti coveche gore-desno'] = (new_player, ball)

        new_player = chovecheDoluDesno(player, ball, self.enemy_territory)
        if new_player != player:
            successors['Pomesti coveche dolu-desno'] = (new_player, ball)

        new_player, new_ball = topkaGore(player, ball, self.enemy_territory)
        if new_ball != ball:
            successors['Turni topka gore'] = (new_player, new_ball)

        new_player, new_ball = topkaDolu(player, ball, self.enemy_territory)
        if new_ball != ball:
            successors['Turni topka dolu'] = (new_player, new_ball)

        new_player, new_ball = topkaDesno(player, ball, self.enemy_territory)
        if new_ball != ball:
            successors['Turni topka desno'] = (new_player, new_ball)

        new_player, new_ball = topkaGoreDesno(player, ball, self.enemy_territory)
        if new_ball != ball:
            successors['Turni topka gore-desno'] = (new_player, new_ball)

        new_player, new_ball = topkaDoluDesno(player, ball, self.enemy_territory)
        if new_ball != ball:
            successors['Turni topka dolu-desno'] = (new_player, new_ball)

        return successors

    def h(self, node):
        x1, y1 = node.state[1]
        closest_distance = float('inf')

        for goal in self.goal_coordinates:
            x2, y2 = goal
            distance = abs(x2 - x1) + abs(y2 - y1)
            closest_distance = min(closest_distance, distance)

        return closest_distance / 2

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal_coordinates


if __name__ == '__main__':
    player_coordinates = tuple(map(int, input().split(",")))
    ball_coordinates = tuple(map(int, input().split(",")))

    goal_coordinates = ((7, 2), (7, 3))

    enemy_territory = (
        (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2),
        (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5), (6, 3),
        (6, 4), (6, 5))

    goal_problem = Goal(enemy_territory, goal_coordinates, (player_coordinates, ball_coordinates))

    goal_problem_solution = astar_search(goal_problem)

    if goal_problem_solution is not None:
        print(goal_problem_solution.solution())
