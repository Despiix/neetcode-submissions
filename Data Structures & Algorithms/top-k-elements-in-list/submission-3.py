from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        res = Counter(nums)

        res_sort = dict(sorted(res.items(), key=lambda x: x[1], reverse = True))

        return list(res_sort)[: k]

