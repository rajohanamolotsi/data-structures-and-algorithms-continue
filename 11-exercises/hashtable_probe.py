class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, idx):
        h = self.get_hash(idx)
        original_h = h
        probing = 0
        while self.arr[h] is not None:
            if self.arr[h][0] == idx:
                return self.arr[h][1]
            probing += 1
            h = (original_h + probing) % self.MAX

        raise KeyError("Index not found")

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        original_h = h
        probing = 0
        while self.arr[h] is not None:
            probing += 1
            h = (original_h + probing) % self.MAX

        self.arr[h] = (key, value)


    def __delitem__(self, key):
        h = self.get_hash(key)
        original_h = h
        probing = 0
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                del self.arr[h]
                return
            probing += 1
            h = (original_h + probing) % self.MAX

        raise KeyError("Key not found")