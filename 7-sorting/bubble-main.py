if __name__ == '__main__':
    elements = [4, 5, 6, 7, 2, 3, 9, 0]
    sorted_elements = []
    count = 0
    print(f'starting point - count: {count}, len(elements): {len(elements)}')
    while count != len(elements) - 1:
        for _ in range(count, len(elements) - 1):
            if count + 1 > 7:
                break
            else:
                if elements[count] < elements[count + 1]:
                    sorted_elements.append(elements[count])
        print(count + 1)
        count += 1

    print(sorted_elements)