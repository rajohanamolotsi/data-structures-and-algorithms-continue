def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    fib_nums = []
    idx = 2
    while fibonacci(idx) < 4000000:
        fib_nums.append(fibonacci(idx))
        idx += 1

    even_numbers = []

    for nums in fib_nums:
        if nums % 2 == 0:
            even_numbers.append(nums)

    sum_even_numbers = 0
    for evens in even_numbers:
        sum_even_numbers += evens

    print(f'fib_num: {fib_nums}')
    print(f'even_numbers: {even_numbers}')
    print(f'sum_even_numbers: {sum_even_numbers}')