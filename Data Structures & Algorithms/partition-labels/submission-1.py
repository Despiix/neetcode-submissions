class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seen = []
        end, size = 0, 0
        last ={}

        for i in range(len(s)):
            last[s[i]] = i
        
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])

            if i == end:
                seen.append(size)
                size = 0
        return seen

        
        


                


