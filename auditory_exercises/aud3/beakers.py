from searching_framework import Problem, breadth_first_graph_search


class BeakersProblem(Problem):
    def __init__(self, capacity, initial, goal):
        super().__init__(initial, goal)
        self.capacity = capacity

    def action_empty(self, state, source):
        if state[source] == 0: return None
        new_state = list(state)
        new_state[source] -= 1
        return tuple(new_state)

    def action_transfer(self, state, source, dest):
        if state[source] == 0 or state[dest] == self.capacity[dest]:
            return None
        new_state = list(state)
        new_state[source] -= 1
        new_state[dest] += 1
        return tuple(new_state)

    def successor(self, state):
        neighbors = dict()

        res1 = self.action_empty(state, 0)
        if res1 is not None: neighbors["Empty_from_0"] = res1

        res2 = self.action_empty(state, 1)
        if res2 is not None: neighbors["Empty_from_1"] = res2

        res3 = self.action_transfer(state, 0, 1)
        if res3 is not None: neighbors["Transfer_from_0_to_1"] = res3

        res4 = self.action_transfer(state, 1, 0)
        if res4 is not None: neighbors["Transfer_from_1_to_0"] = res4

        return neighbors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    capacity = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    initial = tuple(map(int, input().split()))
    problem = BeakersProblem(capacity, initial, goal)
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
