class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 3 # used '+' self.get_level() instead of '*' self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

if __name__ == '__main__':
    pass