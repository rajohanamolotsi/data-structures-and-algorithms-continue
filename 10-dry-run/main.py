class BinarySearchTreeNode:
    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):

        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = self.left.add_child(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = self.right.add_child(data)

    def search(self, value):

        if value == self.data:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        elif value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            

    def delete(self, data):

        if data < self.data:
            if self.left:
                return self.left.delete(data)
        elif data > self.data:
            if self.right:
                return self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
        min_value = self.right.find_min()
        self.right = min_value
        min_value = self.right.delete(min_value)



    def find_min(self):
        if self.left is None:
            return self.data
        return self.left
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right


class TreeNode:
    def __init__(self, data):

        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

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

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1] = node2
        self.graph[node2] = node1

    def print_tree(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')

    def get_neightbours(self, node):
        if node in self.graph:
            return self.graph.get(node, []) # chech if it is print or return
        
    def has_edges(self, node1, node2):
        return node2 in self.graph.get(node1, [])
    

if __name__ == '__main__':
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.print_tree()

    root = TreeNode("Favourites")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Samsung"))
    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("Mecer"))

    phones = TreeNode("Phones")
    phones.add_child(TreeNode("Samsung"))
    phones.add_child(TreeNode("iPhone"))
    phones.add_child(TreeNode("Google Pixel"))

    cars = TreeNode("Cars")
    cars.add_child(TreeNode("Mercedes-Benz"))
    cars.add_child(TreeNode("BMW"))
    cars.add_child(TreeNode("VW"))

    root.add_child(cars)
    root.add_child(laptop)
    root.add_child(phones)

    root.print_tree()