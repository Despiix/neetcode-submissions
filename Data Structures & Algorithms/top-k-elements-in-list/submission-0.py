from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        same = []

        top_k = [key for key, _ in sorted(counter.items(), key=lambda item: item[1], reverse=True)[:k]]        
        return top_k


