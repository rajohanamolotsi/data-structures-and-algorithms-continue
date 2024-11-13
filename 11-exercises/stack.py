from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
def reverse_string(string_words):
    s = Stack()
    reversed_string = ''
    for char in string_words:
        s.push(char)
    while not s.is_empty():
        reversed_string += s.pop()
    return reversed_string

def is_match(opening, closing):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    return match_dict[closing] == opening

def is_balanced(expr):
    s = Stack()
    for char in expr:
        if char == '(' or char == '[' or char == '{':
            s.push(char)
        elif char == ')' or char == ']' or char == '}':
            if s.is_empty() or not is_match(s.pop(), char):
                return False
            
    return s.size() == 0

if __name__ == '__main__':

    print(reverse_string("We will conquere COVID-19"))
    
    tests = [
        "({a+b})",
        "))((a+b}{",
        "((a+b))",
        "))",
        "[a+b]*(x+2y)*{gg+kk}"
    ]

    for expr in tests:
        print(is_balanced(expr))