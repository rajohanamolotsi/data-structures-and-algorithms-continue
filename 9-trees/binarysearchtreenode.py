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
                self.left = BinarySearchTreeNode(data)


        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, value):
        if value == self.data:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
            
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements
    
    def delete(self, value):

        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        if value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.left
        
        min_value = self.left.find_min()
        self.data = min_value
        self.left = self.left.delete(min_value)

        return self


    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()