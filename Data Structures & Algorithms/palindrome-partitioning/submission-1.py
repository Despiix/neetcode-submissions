class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_pal(sub):
            return sub == sub[::-1]

        def dfs(i):
            if i == len(s):
                res.append(path.copy())
                return
            for j in range(i + 1, len(s) + 1):
                if is_pal(s[i: j]):
                    path.append(s[i:j])
                    dfs(j)
                    path.pop()
            

        dfs(0)
        return res
            