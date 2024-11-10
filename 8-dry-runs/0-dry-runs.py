def linear(data, target):

    for idx, element in enumerate(data):
        if element == target:
            return idx
        
    return -1

def binary(data, target):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    data = [2, 3, 4, 6, 7, 8, 10]
    print(linear(data, 6))
    print(binary(data, 6))