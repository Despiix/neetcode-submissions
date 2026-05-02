from itertools import product

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if any(n <= 0 for n in nums):
            curMin, curMax = 1, 1
            res = max(nums)

            for n in nums:
                tmp = curMax * n
                curMax = max(curMax * n, curMin * n, n)
                curMin = min(tmp, curMin * n, n)
                res = max(res, curMax)
            return res


        else:
            return math.prod(nums)
