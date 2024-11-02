def selection_sort(data):
    for idx_I in range(size - 1):
        min_idx = idx_I
        for idx_J in range(min_idx + 1, size):
            if data[idx_J] < data[min_idx]:
                min_idx = idx_J

        if idx_I != min_idx:
            data[idx_I], data[min_idx] = data[min_idx], data[idx_I]


if __name__ == '__main__':
    data = [5, 9, 2, 1, 67, 34, 88, 34]
    size = len(data)
    selection_sort(data)
    print(data)