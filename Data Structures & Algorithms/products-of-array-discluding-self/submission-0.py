class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_with_no_zeros = 1
        zero_count = 0
        ans = []
        for i in nums: 
            if i != 0:
                product_with_no_zeros *= i
            else: 
                zero_count += 1
        if zero_count > 1: 
            return [0] * len(nums)
        elif zero_count == 1:
            for i in nums:
                if i != 0:
                    ans.append(0)
                else:
                    ans.append(product_with_no_zeros)
        else:
            for i in nums:
                ans.append(product_with_no_zeros // i)
        return ans
            