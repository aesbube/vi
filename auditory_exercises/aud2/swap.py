def swap(list):
    return [(item2, item1) for item1, item2 in list]


if __name__ == '__main__':
    length = int(input("Enter the length of the list: "))

    sample_list = []
    for _ in range(length):
        first = input("Enter the first element of the tuple: ")
        second = input("Enter the second element of the tuple: ")
        sample_list.append((first, second))

    print("The unmodified list is: ", sample_list)
    result = swap(sample_list)
    print("The modified list is: ", result)
