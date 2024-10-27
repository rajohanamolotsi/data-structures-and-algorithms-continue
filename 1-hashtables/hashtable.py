class HashTable:
    def __init__(self, max):
        self.MAX = max
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = (key, value)

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = []