class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            l, r = i, i + 1
            res = self.ispal(s, l, r, res)

            l, r = i, i
            res = self.ispal(s, l, r, res)

        return res

    def ispal(self, s, l, r, res):  
        while(l >=0 and r < len(s) and s[l] == s[r]):
            res += 1

            r += 1
            l -= 1
        
        return res
