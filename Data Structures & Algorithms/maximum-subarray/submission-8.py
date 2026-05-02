class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, tsum = 0, nums[0]

        for i in range(len(nums)):           
            if cursum < 0:
                cursum = 0    

            cursum += nums[i]           
            
            tsum = max(cursum, tsum)

        return tsum 