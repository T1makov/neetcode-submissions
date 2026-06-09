class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(s) != len(t):
            return False
        else: 
            for i in s: 
                if i in dict:
                    dict[i] += 1
                else:
                    dict[i] = 1
            for i in t:
                if i not in dict:
                    return False
                else: 
                    dict[i] -= 1
                if dict[i] < 0:
                    return False 
           
            return True