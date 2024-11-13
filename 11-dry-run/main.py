from hashtable import Hashtable

if __name__ == '__main__':
    t = Hashtable()
    my_dict = {}
    with open('stock_prices.csv', 'r') as f:
        for line in f:
            tokens = line.split(',')
            my_dict[tokens[0]] = tokens[1]

    print(t.arr, my_dict)