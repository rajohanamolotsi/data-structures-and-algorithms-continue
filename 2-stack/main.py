from stack import Stack

if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(6)

    print(s.peek())

    s.pop()
    s.pop()
    s.pop()

    print(s.size())

    s.pop()