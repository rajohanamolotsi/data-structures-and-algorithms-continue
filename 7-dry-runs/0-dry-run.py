def bubble_sort(data):
    size = len(data)
    swapped = False
    for idx_I in range(size - 1):
        for idx_J in range(size - 1 - idx_I):
            if data[idx_J + 1] < data[idx_J]:
                temp = data[idx_J + 1]
                data[idx_J + 1] = data[idx_J]
                data[idx_J] = temp
                swapped = True

        if not swapped:
            break

        

def selection_sort(data):
    size = len(data)
    for idx_I in range(size - 1):
        min_idx = idx_I
        for idx_J in range(min_idx + 1, size):
            if data[min_idx] > data[idx_J]:
                min_idx = idx_J

        if idx_I != min_idx:
            data[idx_I], data[min_idx] = data[min_idx], data[idx_I]

def insertion_sort(data):
    size = len(data)
    for idx_I in range(1, size):
        idx_J = idx_I
        while idx_J > 0 and data[idx_J - 1] > data[idx_J]:
            data[idx_J], data[idx_J - 1] = data[idx_J - 1], data[idx_J]
            idx_J -= 1

def merge_two_sorted_lists(left, right, data):
    len_left = len(left)
    len_right = len(right)

    i = j = k = 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
            k += 1
        else:
            data[k] = right[j]
            j += 1
            k += 1

    while i < len_left:
        data[k] = left[i]
        i += 1
        k += 1

    while j < len_right:
        data[k] = right[j]
        j += 1
        k += 1

    return data

def merge_sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2

    left = data[:mid]
    right = data[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_lists(left, right, data) 

if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28, 22, 21, 77, 99]
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    print(merge_sort(arr))