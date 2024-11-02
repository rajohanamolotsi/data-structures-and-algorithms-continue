if __name__ == '__main__':
    elements = [4, 5, 6, 7, 2, 3, 9, 0]
    size = len(elements)
    for temp_idx in range(size - 1):
        swapped = False
        for idx in range(size - 1 - temp_idx):
            '''
            The reason why temp_idx goes from 0 - 6 i is because
             we know that the biggest number will bubble itself up to
              the last element, and it will get there by element[temp_idx + 1] (because
               when it gets to temp_idx = 6, temp_idx + 1 = 7 which is the last index of the list)
            '''
            if idx == 0:
                print('===================================')
            print(f'size - 1: {size - 1} | temp_idx: {temp_idx} | idx: {idx}')