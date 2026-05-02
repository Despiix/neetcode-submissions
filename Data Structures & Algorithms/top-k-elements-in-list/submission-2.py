class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        

        cnt = Counter()
        for n in nums:
            cnt[n] += 1

        cnt_items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

        return [num for num, freq in cnt_items[:k]]

