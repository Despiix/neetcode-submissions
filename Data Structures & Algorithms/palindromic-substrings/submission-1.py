class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res = self.ispal(i, i, res, s)       # odd length
            res = self.ispal(i, i + 1, res, s)   # even length
 
        return res
        

    def ispal(self, l, r, res, s):
        while l >=0 and r < len(s) and s[l] == s[r]:
            res += 1

            l -= 1
            r += 1
    
        return res
