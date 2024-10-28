if __name__ == '__main__':
    '''
    PROBLEM:

    You are given two strings 'STR 1' and ' STR 2' .
      Your task is to find if 'STR 1' is a subsequence of
        'STR 2' . A subsequence of a string is a new string
          that can be derived from the original string by deleting
            some characters without changing the relative ordering of other characters
    '''
    STR1 = ['A', 'C', 'E']
    STR2 = ['A', 'B', 'C', 'D', 'E']
    # Tested it with STR1 = ['A', 'E', 'C']
    order = []
    for i in STR2:
        for j in STR1:
            if i == j:
                order.append(j)
    if order == STR1:
        print(True)
    else:
        print(False)