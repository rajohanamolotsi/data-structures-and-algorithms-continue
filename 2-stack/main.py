from stack import Stack

def reverse_string(string):
    s = Stack()
    revString = ''
    for char in string:
        s.push(char)
    for revChar in range(s.size()):
        revString += s.pop()
    return revString

if __name__ == '__main__':
    print(reverse_string("We will conquere COVID-19"))