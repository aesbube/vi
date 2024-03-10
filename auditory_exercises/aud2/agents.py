from random import randint


class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Position: ({self.x}, {self.y})"

    def move(self):
        pass


class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == '__main__':
    first_coordinate = randint(-10, 10)
    second_coordinate = randint(-10, 10)

    la = LeftAgent(first_coordinate, second_coordinate)
    print(la)
    for i in range(5):
        la.move()
        print(f'Position in step {i + 1} : {la}')

    first_coordinate = randint(-10, 10)
    second_coordinate = randint(-10, 10)

    ra = RightAgent(first_coordinate, second_coordinate)
    print(ra)
    for i in range(5):
        ra.move()
        print(f'Position in step {i + 1} : {ra}')

    first_coordinate = randint(-10, 10)
    second_coordinate = randint(-10, 10)

    ua = UpAgent(first_coordinate, second_coordinate)
    print(ua)
    for i in range(5):
        ua.move()
        print(f'Position in step {i + 1} : {ua}')

    first_coordinate = randint(-10, 10)
    second_coordinate = randint(-10, 10)

    da = DownAgent(first_coordinate, second_coordinate)
    print(da)
    for i in range(5):
        da.move()
        print(f'Position in step {i + 1} : {da}')
