from hashtable import Hashtable

if __name__ == '__main__':
    t = Hashtable()
    with open('stock_prices.csv', 'r') as f:
        for line in f:
            tokens = line.split(',')
            t[tokens[0]] = tokens[1]

    print(t.arr)