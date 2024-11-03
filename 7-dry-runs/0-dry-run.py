def bubble_sort(data):
    size = len(data)
    swapped = False
    for idx_I in range(size - 1):
        for idx_J in range(size - 1 - idx_I):
            if data[idx_J + 1] < data[idx_J]:
                temp = data[idx_J + 1]
                data[idx_J + 1] = data[idx_J]
                data[idx_J] = temp
                swapped = True

        if not swapped:
            break

        

def selection_sort(data):
    size = len(data)
    for idx_I in range(size - 1):
        min_idx = idx_I
        for idx_J in range(min_idx + 1, size):
            if data[min_idx] > data[idx_J]:
                min_idx = idx_J

        if idx_I != min_idx:
            data[idx_I], data[min_idx] = data[min_idx], data[idx_I]

def insertion_sort(data):
    size = len(data)
    for idx_I in range(1, size):
        idx_J = idx_I
        while idx_J > 0 and data[idx_J - 1] > data[idx_J]:
            data[idx_J], data[idx_J - 1] = data[idx_J - 1], data[idx_J]
            idx_J -= 1

if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for arr in tests:
        bubble_sort(arr)
        print(f'sorted_arr: {arr}')