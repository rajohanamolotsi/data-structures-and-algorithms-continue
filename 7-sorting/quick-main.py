def partition(data, start, end):
    pivot = data[start]
    leftwall = start

    for idx in range(start + 1, end + 1): # mark
        if data[idx] < pivot: # mark
            leftwall += 1
            data[idx], data[leftwall] = data[leftwall], data[idx]

    data[start], data[leftwall] = data[leftwall], data[start]
    
    return leftwall # mark

def quick_sort(data, start, end):
    if start < end:
        pivot_idx = partition(data, start, end) # mark
        quick_sort(data, start, pivot_idx - 1)
        quick_sort(data, pivot_idx + 1, end)

if __name__ == '__main__':
    data = [29, 10, 14, 37, 13]
    start = 0
    end = len(data) - 1
    quick_sort(data, start, end)
    print(data)