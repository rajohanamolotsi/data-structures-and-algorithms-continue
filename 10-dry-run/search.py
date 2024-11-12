def linear(data, target):

    for idx, element in enumerate(data):
        if element == target:
            return idx
        
    return -1

def binary(data, target):

    size = len(data)

    left, right = 0, size - 1

    while left < right:

        mid = (left + right) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def recursive_binary(data, left, right, target):

    if right < left:
        return -1

    mid = (left + right) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    return recursive_binary(data, left, right, target)

if __name__ == '__main__':

    target = 7

    tests = [
        [1, 3, 5, 7, 9],
        [2, 4, 6, 7, 8, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    for data in tests:
        print(f'linear: {linear(data, target)}')
        print(f'binary: {linear(data, target)}')

    data = tests[0]
    left, right = 0, len(data)

    print(f'recursive_binary_1: {recursive_binary(data, left, right, target)}')

    data = tests[1]
    left, right = 0, len(data)

    print(f'recursive_binary_2: {recursive_binary(data, left, right, target)}')

    data = tests[2]
    left, right = 0, len(data)

    print(f'recursive_binary_3: {recursive_binary(data, left, right, target)}')