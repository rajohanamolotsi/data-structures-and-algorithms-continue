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
            data[idx], data[leftwall] = data[leftwall], data[idx]
            leftwall += 1

    data[low], data[leftwall] = data[leftwall], data[low]
    return leftwall

def shell_sort(data):
    size = len(data)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            temp = data[i]
            j = i

            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp

        gap //= 2


def bubble_sort(data):
    size = len(data)
    for i in range(size - 1):
        j = i
        swapped = False
        for j in range(size - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                j -= 1 # check

        if not swapped:
            break

def selection_sort(data):
    size = len(data)
    for i in range(size - 1): # check
        min_idx = i
        for j in range(min_idx + 1, size):
            if data[j] < data[min_idx]:
                min_idx = j

        if min_idx != i:
            data[min_idx], data[i] = data[i], data[min_idx]

def insertion_sort(data):
    size = len(data)
    for i in range(1, size):
        j = i
        while j > 0 and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


if __name__ == '__main__':

    data = [29, 10, 14, 37, 13]

    insertion_sort(data)
    print(data)