def factorial(n):
    if n == 0:
        # print(f'n: {n}')
        # print(f'n - 1: {n - 1}')
        return 1
    else:
        # print(f'n, n - 1: {n, n - 1}')
        print(f'factorial(n - 1): {factorial(n - 1)}')
        return n * factorial(n - 1)
    
if __name__ == '__main__':
    factorial(3)