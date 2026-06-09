class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_dic = {} 
        ans_list = []
        for num in nums:
            if num in ans_dic:
                ans_dic[num] += 1
            else:
                ans_dic[num] = 1
        keys = sorted(ans_dic, key=ans_dic.get, reverse=True)
        return keys[:k]
        