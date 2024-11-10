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

if __name__ == '__main__':
    data = [2, 3, 4, 5, 7, 8]
    print(binary(data, 4))