from searching_framework import Problem, breadth_first_graph_search


class Molecules(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.rows = 7
        self.colums = 9
        self.matrix = (
            (0, 0, 0, 1, 0, 1, 0, 1, 0),
            (0, 0, 1, 0, 0, 0, 0, 0, 1),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
            (0, 1, 0, 0, 0, 0, 1, 1, 0),
            (0, 0, 0, 0, 1, 0, 1, 0, 0),
            (1, 1, 0, 1, 0, 0, 1, 0, 0),
            (0, 0, 0, 0, 0, 0, 0, 0, 0),
        )

    def goal_test(self, state):
        atom1, atom2, atom3 = state
        return atom1[0] + 1 == atom2[0] and atom2[0] + 1 == atom3[0] \
            and atom1[1] == atom2[1] and atom2[1] == atom3[1]

    def succesor(self, state):
        neighbors = dict()

        actions = ("Right", "Left", "Up", "Down")
        directions = ((+1, 0), (-1, 0), (0, +1), (0, -1))

        for action, direction in zip(actions, directions):
            for i in range(3):
                action_name = action + str(i)
                res = self.move(state, direction, i)
                if res != None:
                    neighbors[action_name] = res

        return neighbors

    def move(self, state, direction, ind):
        atom_to_move = state[ind]
        new_atom = self.change_atom_direction(atom_to_move, direction)

        new_state = list(state)
        new_state[ind] = new_atom
        new_state = tuple(new_state)
        if not self.check_validity_of_state(new_state):
            return None

        end_state = self.move(new_state, direction, ind)

        if end_state is None:
            return new_state
        else:
            return end_state

    def change_atom_direction(self, atom, direction):
        atom = list(atom)
        atom[0] = direction[0]
        atom[1] = direction[1]

        return tuple(atom)

    def check_validity_of_state(self, state):
        for atom in state:
            x, y = atom
            if 0 <= x <= self.colums and 0 <= y <= self.rows:
                return False
            if self.matrix[x][y] == 1:
                return False
            if len(set(state)) == 3:
                return True
        return False


if __name__ == '__main__':
    atom_1 = tuple(map(int, input().split()))
    atom_2 = tuple(map(int, input().split()))
    atom_3 = tuple(map(int, input().split()))
    # i.e.:      atom_1,atom_2,atom_3 = \
    #   map( lambda _: map(int, input().split()), range(3) )

    problem = Molecules((atom_1, atom_2, atom_3))
    node = breadth_first_graph_search(problem)
    if node is not None:
        print(node.solution())
        print(node.solve())
        print(node.path())
        actions, states = node.solution(), node.solve()
        print(states[0])
        for action, state in zip(actions, states[1:]):
            print(action, state, sep="\n")
    else:
        print("Cannot be solved")
