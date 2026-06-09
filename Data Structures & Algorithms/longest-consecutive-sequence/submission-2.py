class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        largest_sequence = 1
        current_sequence = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                pass
            elif nums[i] - nums[i-1] == 1:
                current_sequence += 1
                if current_sequence > largest_sequence:
                    largest_sequence = current_sequence
            else:
                current_sequence = 1
        return largest_sequence
