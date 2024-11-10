def bubble_sort(data):
    size = len(data)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True # forgot
                # check: j -= 1

        if not swapped:
            break

def selection_sort(data):
    size = len(data)
    for i in range(size - 1):
        min_idx = i
        for j in range(min_idx + 1, size):
            if data[j] < data[min_idx]:
                min_idx = j
                j -= 1 # check

        if i != min_idx:
            data[i], data[min_idx] = data[min_idx], data[i]

def insertion_sort(data):
    size = len(data)
    for i in range(1, size):
        j = i
        while j > 0 and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1

def merge_sort(data):
    size = len(data)
    if size <= 1:
        return data
    
    mid = size // 2

    left = data[:mid]
    right = data[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_the_sort(data, left, right)

def merge_the_sort(data, left, right):
    len_left = len(left)
    len_right = len(right)

    i = j = k = 0

    while i < len_left and j < len_right: # forgetten to use lengths instead of left[i] ...
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
            k += 1
        else:
            data[k] = right[j]
            j += 1
            k += 1

    while i < len_left: # also here
        data[k] = left[i]
        i += 1
        k += 1

    while j < len_right: # also here
        data[k] = right[j]
        j += 1
        k += 1


def quick_sort(data, low, high):
    if low < high:
        pivot_idx = partition_sort(data, low, high)
        quick_sort(data, low, pivot_idx - 1)
        quick_sort(data, pivot_idx + 1, high)

def partition_sort(data, low, high):
    pivot = data[low]
    leftwall = low

    for idx in range(low + 1, high + 1):
        if data[idx] < pivot:
            leftwall += 1 # put it here instead of after below, makes it a huge difference
            data[idx], data[leftwall] = data[leftwall], data[idx]

    data[low], data[leftwall] = data[leftwall], data[low]
    return leftwall

def shell_sort(data):
    size = len(data)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp: # had forgotten to use temp instead of j and j - gap
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp

        gap //= 2

if __name__ == '__main__':
    
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for data in tests:
        quick_sort(data, low = 0, high = len(data) - 1)
        print(f'data: {data}')