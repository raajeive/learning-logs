class MyHashSet:

    def __init__(self):
        self.hashSet = set()
        
    def add(self, key):
        self.hashSet.add(key)

    def remove(self, key):
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key):
        return key in self.hashSet
