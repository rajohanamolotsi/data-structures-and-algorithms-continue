from queue import Queue

if __name__ == '__main__':
    q = Queue()

    q.enqueue({
        'Company': 'Wall Mart',
        'Timestamp': '15 Apr., 11:01 AM',
        'Price': 131.10
    })

    q.enqueue({
    'Company': 'Wall Mart',
    'Timestamp': '15 Apr., 11.02 AM',
    'Price': 132.00
    })

    q.enqueue({
        'Company': 'Wall Mart',
        'Timestamp': '15 Apr., 11.03 AM',
        'Price': 135.00
    })

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.size())
    print(q.is_empty())