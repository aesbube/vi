def element_val(element, i, n):
    if i < n / 2:
        return element * 2
    else:
        return element * 3


if __name__ == '__main__':
    user_input = input().split(" ")
    n = int(user_input[0])
    m = int(user_input[1])

    elements_array = [int(i) for i in user_input[2:]]

    elements_matrix = [elements_array[i:i + m] for i in range(0, len(elements_array), m)]

    result_matrix = [[element_val(elements_matrix[i][j], i, n) for j in range(0, m)] for i in range(0, n)]
    print(result_matrix)
