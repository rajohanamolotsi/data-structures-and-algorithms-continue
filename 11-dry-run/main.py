from hashtable import HashTable

if __name__ == '__main__':
    t = HashTable()
    with open('stock_prices.csv', 'r') as f:
        for line in f:
            tokens = line.split(',')
            t[tokens[0]] = tokens[1]

    for element in t.arr:
        print(element)