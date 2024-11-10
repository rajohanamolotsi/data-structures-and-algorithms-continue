def linear(data, target):
    for idx, element in enumerate(data):
        print(idx, element)
        if element == target:
            return idx
        
    return -1

if __name__ == '__main__':
    data = [2, 4, 6, 8]
    print(linear(data, 2))