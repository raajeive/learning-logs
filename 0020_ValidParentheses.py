class stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.array = []
    
    def push(self, val):
        if self.size < self.capacity:
            self.array.append(val)
            self.size += 1
            return val
        else:
            return False
    
    def pop(self):
        if self.size > 0:
            temp = self.array.pop()
            self.size -= 1
            return temp
        else:
            return False
    
    def top(self):
        if self.size > 0:
            return self.array[self.size - 1]
        else:
            return False
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


class Solution:
    def isValid(self, s):
        strstack = stack(len(s))
        for letter in s:
            if letter in ["(", "{", "["]:
                strstack.push(letter)
            else:
                if (letter == ")" and strstack.top() == "(") or (letter == "}" and strstack.top() == "{") or (letter == "]" and strstack.top() == "["):
                    strstack.pop()
                else:
                    return False
        if strstack.is_empty():
            return True
        else:
            return False
