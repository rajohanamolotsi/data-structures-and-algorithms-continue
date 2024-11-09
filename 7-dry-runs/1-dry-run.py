def merge_sort(data):
    size = len(data)

    if size <= 1:
        return data
    
    mid = size // 2
    left = data[:mid]
    right = data[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_the_two(left, right, data)

def merge_the_two(left, right, data):
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
        pivot_idx = partition(data, low, high)
        quick_sort(data, low, pivot_idx - 1)
        quick_sort(data, pivot_idx + 1, high)


def partition(data, low, high):
    pivot = data[low]
    leftwall = low

    for idx in range(low + 1, high + 1):
        if data[idx] < pivot:
            leftwall += 1
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
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp

        gap //= 2

if __name__ == '__main__':

    data = [29, 10, 14, 37, 13]

    quick_sort(data, 0, len(data) - 1)
    print(data)