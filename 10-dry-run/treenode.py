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
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        for child in self.children:
            child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

if __name__ == '__main__':
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Samsung"))
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("DELL"))

    phones = TreeNode("Phones")
    phones.add_child(TreeNode("iPhone 16 Pro Max"))
    phones.add_child(TreeNode("Samsung Note"))
    phones.add_child(TreeNode("Google Pixel"))

    root.add_child(phones)
    root.add_child(laptop)

    root.print_tree()