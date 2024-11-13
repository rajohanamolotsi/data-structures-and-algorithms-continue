class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
        if not found:
            self.arr.append((key, value))
            

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr):
            if element[0] == key:
                print('del', idx)
                del self.arr[h][idx]