if __name__ == '__main__':
    user_input = input().split(" ")
    n = int(user_input[0])
    m = int(user_input[1])

    elements_array = [int(i) for i in user_input[2:]]

    elements_matrix = [elements_array[i:i + m] for i in range(0, len(elements_array), m)]

    result_matrix = [elem * 2 for row in elements_matrix for elem in row]
    # the output is an array of the elements
    print(result_matrix)

    result_matrix_1 = [[elements_matrix[i][j] * 2 for j in range(0, m)] for i in range(0, n)]
    # the output is an
    # array with the rows as elements
    print(result_matrix_1)
