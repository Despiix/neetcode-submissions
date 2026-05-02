class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) <= 0:
            return '-1'

        string = str(len(strs[0])) + '#' + strs[0]
        
        for i in range(1, len(strs)):
            string += str(len(strs[i])) + '#' + strs[i]
        return string

    def decode(self, s: str) -> List[str]:
        if s == '-1':
            return []

        res, i = [], 0

        while i < len(s):
            j = s.index('#', i)
            lenght = int(s[i:j])
            res.append(s[j+1: j+1+lenght])
            i = j + lenght + 1
        return res



