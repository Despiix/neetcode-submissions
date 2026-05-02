class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, tsum = 0, 0

        neg = all(val < 0 for val in nums)
        if neg:
            return max(nums)

        for i in range(len(nums)):
            cursum += nums[i]
            
            if cursum < 0:
                cursum = 0               
            
            tsum = max(cursum, tsum)

        return tsum 