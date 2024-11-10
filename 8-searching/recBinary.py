def binary(data, left, right, target):

    if right < left:
        return -1
    
    mid = (left + right) // 2
    
    if mid < 0 or mid > len(data):
        return -1

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    return binary(data, left, right, target)

if __name__ == '__main__':
    data = [2, 3, 4, 5, 6, 7, 8, 99]
    left = 0
    right = len(data) - 1
    target = 99
    print(binary(data, left, right, target))