def insertion_sort(data):
    size = len(data) # 6 elements
    for idx_I in range(1, size):
        idx_J = idx_I
        while idx_J > 0 and data[idx_J - 1] > data[idx_J]:
            data[idx_J], data[idx_J - 1] = data[idx_J - 1], data[idx_J]
            idx_J = idx_J - 1


if __name__ == '__main__':
    data = [11, 9, 29, 7, 2, 15, 28]
    # data = [2, 8, 5, 3, 9, 4] # 0 - 5 elements
    tests = [
        data,
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for elements in tests:
        insertion_sort(elements)
        print(f'sorted list: {elements}')