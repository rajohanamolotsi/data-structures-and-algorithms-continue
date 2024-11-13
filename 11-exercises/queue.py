from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) == 0
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue("1")
    front = q.front()
    for _ in range(10):
        front = q.front()
        print(front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        q.dequeue()