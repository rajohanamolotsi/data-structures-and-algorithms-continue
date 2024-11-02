if __name__ == '__main__':
    data = [5, 9, 2, 1, 67, 34, 88, 34]
    size = len(data)
    for idx_I in range(size - 1):
        print(f'min_idx, idx_I: {idx_I}')
        min_idx = idx_I
        print('===========================================================')
        for idx_J in range(min_idx + 1, size):
            print(f'idx_J: {idx_J}')
            if data[idx_J] < data[min_idx]:
                print(f'data[idx_J]: {data[idx_J]} | data[min_idx]: {data[min_idx]}')
                min_idx = idx_J
                print(f'min_idx: {min_idx} | idx_J: {idx_J}')
        
        print(f'data: {data}')
        print(f'idx_I: {idx_I} | min_idx: {min_idx}')
        if idx_I != min_idx:
            data[idx_I], data[min_idx] = data[min_idx], data[idx_I]

        print(f'data: {data}')

        '''
        It's a Pythonic way of exchanging two values without needing a temporary variable.
            - I am going to use it in Bubble sort
        '''

        '''
        This is style of using prints in between strategically will be super useful when analyzing someone's code and/or models in ML, DL etc.
        '''