class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        for i in range(len(s)):
            # odd
            l, r = i, i
            res = self.maxpal(s, l, r, res)

            #even
            l, r = i, i + 1
            res = self.maxpal(s, l, r, res)
        
        return res

    def maxpal(self, s, l, r, res):

        while r < len(s) and l >= 0 and s[l] == s[r]:
            if ((r - l) + 1) > len(res):
                res = s[l : r + 1]
            
            r += 1
            l -= 1
    
        return res

                

        
        