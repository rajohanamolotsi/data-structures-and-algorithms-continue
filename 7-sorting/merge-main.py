'''
def merge(arr = [11, 9, 29, 7, 2, 15, 28]):
    size = len(arr) # size: 7
    if size == 1:
        return arr
    print(f'size: {size}')
    arr_1 = arr[0 : (size - 1)/2] # arr[0:3]
    arr_2 = arr[((size - 1)/2) + 1 : size - 1] # arr[4:6]

    print(f'arr_1: {arr_1}, arr_2: {arr_2}')

if __name__ == '__main__':
    merge()


def merge_sort(arr):
    if len(arr) - 1 == 1:
        return arr
    
    if size % 2 == 0:
        first_half = int(size/2)
    else:
        first_half = int(round(size/2))

    for idx_I in range(first_half):


    arr_1 = arr[0 : first_half]
    arr_2 = arr[first_half : size]



if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28, 22, 21, 77, 99]
    size = len(arr)
    first_half = 0
    
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a, b, arr):
    len_left = len(a)
    len_right = len(b)
    
    i = j = k = 0

    while i < len_left and j < len_right:
        if a[i] <= b[j]: # my error was here: if a[i] <= b[j]
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
        print(f'while i < len_left and j < len_right | arr[k]: {arr[k - 1]}')

    while i < len_left:
        arr[k] = a[i]
        i += 1
        k += 1
        print(f'while i < len_left | arr[k]: {arr[k - 1]}')

    while j < len_right:
        arr[k] = b[j]
        j += 1
        k += 1
        print(f'while j < len_right | arr[k]: {arr[k - 1]}')

    return arr

if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28, 22, 21, 77, 99]
    print(merge_sort(arr))