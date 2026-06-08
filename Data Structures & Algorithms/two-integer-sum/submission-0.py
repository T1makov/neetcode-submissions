class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        diff = 0
        for i in range(len(nums)): 
            diff = target - nums[i]
            if nums[i] in dict:
                return [dict[nums[i]], i]
            dict[diff] = i