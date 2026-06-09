class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False 
        stack = []
        for char in s: 
            if char == "}": 
                if not stack: 
                    return False
                if stack.pop() != "{":
                    return False
            elif char == ")": 
                if not stack: 
                    return False
                if stack.pop() != "(":
                    return False
            elif char == "]": 
                if not stack: 
                    return False
                if stack.pop() != "[":
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True

        

        