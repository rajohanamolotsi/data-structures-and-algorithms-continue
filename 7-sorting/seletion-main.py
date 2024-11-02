if __name__ == '__main__':
    data = [5, 9, 2, 1, 67, 34, 88, 34]
    size = len(data)
    for idx_I in range(size - 1):
        min_idx = idx_I
        print('=====================')
        for idx_J in range(min_idx + 1, size):
            print(f'min_idx: {min_idx} | idx_J: {idx_J}')