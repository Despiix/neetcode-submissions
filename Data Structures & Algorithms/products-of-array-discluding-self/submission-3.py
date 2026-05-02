class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, idx = 1, []
        
        if set(nums) == {0}:
            return nums

        if 0 in nums:
            idx = [index for index, value in enumerate(nums) if value == 0]
            out = [0] * len(nums)
            
            for i in range(len(nums)):
                if i not in idx:
                    res = res * nums[i]
            if len(idx) == 1:
                out[idx[0]] = res
        
        else:
            out = []
            for num in nums:
                res = res * num

            for num in nums:
                out.append(int(res/num))
        
        return out