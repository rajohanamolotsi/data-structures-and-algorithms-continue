def linear(data, target):
    for idx, element in enumerate(data):
        if element == target:
            return idx
    return -1

def binary(data, target):
    size = len(data)
    left, right = 0, size - 1

    while left <= right:
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
        return recursive_binary(data, mid + 1, right, target)
    else:
        return recursive_binary(data, left, mid - 1, target)

if __name__ == '__main__':
    tests = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 3, 5, 7, 8, 9, 0],
        [1, 2, 4, 6, 7, 9]
    ]
    
    for data in tests:
        print(f'linear: {linear(data, target=7)}')
        print(f'binary: {binary(data, target=7)}')
        left, right = 0, len(data) - 1
        print(f'recursive: {recursive_binary(data, left, right, target=7)}')