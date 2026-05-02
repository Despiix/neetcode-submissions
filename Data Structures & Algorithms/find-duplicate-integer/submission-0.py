class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums) - 1):
            r = len(nums) - 1
            
            while i < r:
                if nums[r] == nums[i]: 
                    return nums[i]
                else:
                    r -= 1
            