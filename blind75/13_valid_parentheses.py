class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses_map = {")" : "(", "}": "{", "]" : "["}

        open_parentheses = ["(", "{", "["]

        close_parentheses = [")", "}", "]"]

        parentheses_stack = []

        for idx in range(len(s)):
            if s[idx] in open_parentheses:
                parentheses_stack.append(s[idx])
            elif s[idx] in close_parentheses and len(parentheses_stack) > 0 and parentheses_map[s[idx]] == parentheses_stack[-1]:
                parentheses_stack.pop(-1)
            else:
                return False
        
        if len(parentheses_stack) == 0:
            return True
        
        return False
