from searching_framework import *


class Tower_of_hanoi(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        for i, pillar_1 in enumerate(state):
            if len(pillar_1) == 0:
                continue

            top_block = pillar_1[-1]
            for j, pillar_2 in enumerate(state):
                if i == j:
                    continue
                if len(pillar_2) == 0 or top_block <= pillar_2[-1]:
                    successors[f'MOVE TOP BLOCK FROM PILLAR {i + 1} TO PILLAR {j + 1}'] = self.generate_state(state, i,
                                                                                                              j)

        return successors

    def generate_state(self, state, i, j):
        new_state = list(map(list, state))
        top_block = new_state[i].pop()
        new_state[j].append(top_block)

        return tuple(map(tuple, new_state))

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    initial_state = tuple(map(tuple, input().replace(',', '').split(";")))
    goal_state = tuple(map(tuple, input().replace(',', '').split(";")))

    problem = Tower_of_hanoi(initial_state, goal_state)

    problem_solution = breadth_first_graph_search(problem).solution()
    if problem_solution is not None:
        print(f'Number of action {len(problem_solution)}')
        print(problem_solution)
