if __name__ == '__main__':
    data = [2, 8, 5, 3, 9, 4] # 0 - 5 elements
    size = len(data) # 6 elements
    for idx_I in range(1, size - 1):
        print(f'idx_I: {idx_I}')
        print('===========================')
        idx_J = idx_I
        while idx_J > 0 and data[idx_J - 1] > data[idx_J]:
            print(f'idx_J: {idx_J}')
            data[idx_J], data[idx_J - 1] = data[idx_J - 1], data[idx_J]
            idx_J = idx_J - 1