from queue import Queue

def produce_binary_numbers(max):
    q = Queue()
    q.enqueue("1")

    for _ in range(max):
        front = q.front()
        print(front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")

        q.dequeue()


if __name__ == '__main__':

    produce_binary_numbers(10)

    '''
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

    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())

    print(q.front())
    '''