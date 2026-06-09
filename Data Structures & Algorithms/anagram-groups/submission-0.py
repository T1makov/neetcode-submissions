class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        result = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in result_dict:
                result_dict[sorted_word].append(word)
            else: 
                result_dict[sorted_word] = []
                result_dict[sorted_word].append(word)
        for key in result_dict:
            result.append(result_dict[key])
        return result