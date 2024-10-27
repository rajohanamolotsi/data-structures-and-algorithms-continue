class HashTable:
    def __init__(self, max):
        self.MAX = max
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        original_h = h
        probing_count = 0
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            probing_count += 1
            h = (original_h + probing_count) % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        original_h = h
        probing_count = 0
        while self.arr[h] is not None:
            probing_count += 1
            h = (original_h + probing_count) % self.MAX

        self.arr[h] = (key, value)

    def __delitem__(self, key):
        h = self.get_hash(key)
        original_h = h
        probing_count = 0
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                del self.arr[h][1]
            probing_count += 1
            h = (original_h + probing_count) % self.MAX