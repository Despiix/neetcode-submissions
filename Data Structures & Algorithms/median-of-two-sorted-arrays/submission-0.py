class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2 
        res = sorted(res)
        print(res)
        
        n = len(res) - 1
        if (n % 2) != 0:
            avg = (res[n // 2] + res[(n // 2) + 1]) / 2
            return avg
        return res[n // 2]
