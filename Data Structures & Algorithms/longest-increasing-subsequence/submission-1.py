class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n1 = len(nums)
        dp = [1] * (n1) # Max length subseq

        for i in range(n1):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

        