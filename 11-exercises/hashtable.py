class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, idx):
        h = self.get_hash(idx)
        for element in self.arr[h]:
            if element[0] == idx:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                return
        if not found:
            self.arr[h].append((key, value))
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                print('del', idx)
                del self.arr[h][idx]
                return