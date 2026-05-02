class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        dp = {0}
        target = sum(nums) // 2

        for num in nums:
            dp = dp | {s + num for s in dp}
            print(dp)


        return target in dp
