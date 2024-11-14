class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, preference):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if preference == 'name':
            print(prefix + self.name)
            for child in self.children:
                child.print_tree('name')
        elif preference == 'designation':
            print(prefix + self.designation)
            for child in self.children:
                child.print_tree('designation')
        elif preference == 'both':
            print(f'{prefix + self.name} ({self.designation})')
            for child in self.children:
                child.print_tree('both')

if __name__ == '__main__':
    root = TreeNode("Departments", "HOLY TRINITY")

    mathematics = TreeNode("Mathematics", "POWER")
    mathematics.add_child(TreeNode("Linear Algebra", 'LA'))
    mathematics.add_child(TreeNode("Multivariable Calculus", 'MC'))
    mathematics.add_child(TreeNode("Graph Theory", 'GT'))
    english = TreeNode("English", "COMMUNICATION")
    english.add_child(TreeNode("Parts of Speech", 'POS'))
    english.add_child(TreeNode("Listening", 'L'))
    english.add_child(TreeNode("Speaking", 'SP'))
    science = TreeNode("Science", "MIXTURE")
    science.add_child(TreeNode("Physics", 'PHY'))
    science.add_child(TreeNode("Chemistry", 'CHEM'))
    science.add_child(TreeNode("Biology", 'BIO'))

    root.add_child(mathematics)
    root.add_child(english)
    root.add_child(science)

   #  root.print_tree('name')
    root.print_tree('designation')
   #  root.print_tree('both')
