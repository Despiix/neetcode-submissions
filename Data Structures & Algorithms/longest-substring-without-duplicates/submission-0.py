class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        maxsub = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            maxsub = max(maxsub, r - l + 1)
        return maxsub

