from hashtable import HashTable

if __name__ == '__main__':
    t = HashTable(10)
    with open('stock_prices.csv', 'r') as f:
        for line in f:
            tokens = line.split(',')
            t[tokens[0]] = tokens[1].strip()

    for idx in t.arr:
        print(idx)