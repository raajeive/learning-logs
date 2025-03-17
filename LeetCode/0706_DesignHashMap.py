class MyHashMap:
    def __init__(self):
        self.dataDict = {}
        
    def put(self, key, value):
        self.dataDict[key] = value

    def get(self, key):
        if key in self.dataDict:
            return self.dataDict[key]
        return -1

    def remove(self, key):
        if key in self.dataDict:
            del self.dataDict[key]
