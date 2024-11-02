def bubble_sort(data):
    size = len(data)
    swapped = False
    for idx in range(size - 1):
        for swap_idx in range(size - 1 - idx):
            if data[swap_idx] > data[swap_idx + 1]:
                temp = data[swap_idx]
                data[swap_idx] = data[swap_idx + 1]
                data[swap_idx + 1] = temp
                swapped = True

        if not swapped:
            break

        '''
        For a list like [1, 2, 3, 4, 5], which is already sorted,
         no swaps will occur on the first pass. swapped will stay False,
          triggering the break, and ending the sorting process after just
           one pass instead of performing all n - 1 passes.
        '''


if __name__ == '__main__':
    data = ['mona', 'dhaval', 'aamir', 'tina', 'chang']
    # data = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(data)
    print(data)

    for element in data:
        print(f'name: {element[0]}, ord: {ord(element[0])}')
                