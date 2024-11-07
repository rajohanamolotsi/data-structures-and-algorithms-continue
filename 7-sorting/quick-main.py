def partition(data, low, high):
    leftwall = low
    pivot = data[low]

    for idx in range(low + 1, high + 1):
        if data[idx] < pivot:
            leftwall += 1
            data[leftwall], data[idx] = data[idx], data[leftwall]

    data[low], data[leftwall] = data[leftwall], data[low]

    return leftwall

def quick_sort(data, low, high):
    if low < high:
        pivot_idx = partition(data, low, high)
        quick_sort(data, pivot_idx + 1, high)
        quick_sort(data, low, pivot_idx - 1)

if __name__ == '__main__':
    data = [29, 10, 14, 37, 13]
    low = 0
    high = len(data) - 1
    quick_sort(data, low, high)
    print(data)