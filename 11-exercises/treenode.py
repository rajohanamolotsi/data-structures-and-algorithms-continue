class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 1
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, lvl):
        if self.get_level() > lvl:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree(lvl)

if __name__ == '__main__':
    root = TreeNode("Departments")

    mathematics = TreeNode("Mathematics")
    mathematics.add_child(TreeNode("Linear Algebra"))
    mathematics.add_child(TreeNode("Multivariable Calculus"))
    mathematics.add_child(TreeNode("Graph Theory"))

    linear = TreeNode("Linear")
    linear.add_child(TreeNode("Chapter 1"))
    linear.add_child(TreeNode("Chapter 3"))

    english = TreeNode("English")
    english.add_child(TreeNode("Parts of Speech"))
    english.add_child(TreeNode("Listening"))
    english.add_child(TreeNode("Speaking"))

    science = TreeNode("Science")
    science.add_child(TreeNode("Physics"))
    science.add_child(TreeNode("Chemistry"))
    science.add_child(TreeNode("Biology"))

    mathematics.add_child(linear)
    root.add_child(mathematics)
    root.add_child(english)
    root.add_child(science)

    root.print_tree(4)