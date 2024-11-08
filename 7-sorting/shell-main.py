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
    shell_sort(data)
    print(data)