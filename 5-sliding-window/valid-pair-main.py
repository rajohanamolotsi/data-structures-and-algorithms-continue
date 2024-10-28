if __name__ == '__main__':
    '''
    VALID PAIR

    PROBLEM-STATMENT:

    You are given an array 'A' of ' N' integers and
      integers 'K' and 'M’. You need to return true if
        the given array can be divided into pairs such that
          the sum of every pair gives remainder 'M' when divided by 'K'

    WALK THROUGH:

    If the given array is [2,1,5,7] and K = 9 and M = 3.
      Then we need to return true because we can divide the
        array into two pairs i.e (2,1) and (5, 7) whose sums
          are 3 and 12 , which when divided by 9 gives remainder 3,
            thus it is possible to divide the given array into pairs
    '''
    arr = [2, 1, 5, 7]
    len_arr = len(arr)
    K = 9
    M = 3
    pair = []
    # pairs = []
    for element in arr:
        for idx in range(len_arr - 1, -1, -1):
            pair = []
            if (element + arr[idx]) % K == M:
                pair.append(element)
                pair.append(arr[idx])
                print(pair)
            else:
                print(False)

    # print(set(pairs))