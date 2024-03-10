def make_minesweeper(matrix):
    n = len(matrix)
    return [[matrix_check(x, y, matrix) for y in range(n)] for x in range(n)]


def matrix_check(x, y, matrix):
    counter = 0
    if matrix[x][y] == '#':
        return matrix[x][y]
    n = len(matrix)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < n and 0 <= y + j < n:
                if matrix[x + i][y + j] == '#':
                    counter += 1

    return counter


if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input().split("   "))

    matrix = make_minesweeper(matrix)

    for row in matrix:
        print("   ".join(str(col) for col in row))
