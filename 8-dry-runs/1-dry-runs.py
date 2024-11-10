def linear(data, target):

    for idx, element in enumerate(data):
        if element == target:
            return idx
        
    return -1

def binary(data, target):

    left, right = 0, len(data) - 1

    while left < right:
        mid = len(data) // 2
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

    data = [1, 2, 3, 4, 6, 8]

    left, right, target = 0, len(data) - 1, 4

    print(linear(data, target))