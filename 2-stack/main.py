from stack import Stack

def reverse_string(string):
    s = Stack()
    revString = ''
    for char in string:
        s.push(char)
    for revChar in range(s.size()):
        revString += s.pop()
    return revString

def is_match(char1, char2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[char1] == char2

def is_balanced(string):
    s = Stack()
    for char in string:
        if char == '(' or char == '[' or char == '{':
            s.push(char)
        elif char == ')' or char == ']' or char == '}':
            if s.size() == 0:
                return False
            elif not is_match(char, s.pop()):
                return False
            
    return s.size() == 0

if __name__ == '__main__':
    # print(reverse_string("We will conquere COVID-19"))
    # print(reverse_string("I am the king"))

    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))