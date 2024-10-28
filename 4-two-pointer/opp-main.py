if __name__ == '__main__':
    '''
    Input: arr[] = {10, 20, 35, 50}, target =70
    Output:  Yes
    Explanation : There is a pair (20, 50) with given target.
    '''
    tagert = 70
    arr = [10, 20, 35, 50]
    length_arr= len(arr)
    count = 0
    for i in arr:
        for j in range(length_arr - 1, -1, -1):
            if i + arr[j] == tagert:
                print(i, arr[j], True)
            else:
                print(False)