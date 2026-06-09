class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if len(s) != len(t):
            return False
        else: 
            for i in s: 
                if i in dict.keys():
                    dict[i] += 1
                else:
                    dict[i] = 1
            for i in t:
                if i not in dict.keys():
                    return False
                else: 
                    dict[i] -= 1
            for key in dict.keys():
                if dict[key] != 0:
                    return False 
            return True