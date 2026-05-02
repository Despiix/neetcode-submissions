class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        hashmap = {i:[] for i in range(n)}
        visit = [False] * n

        for e, c in edges:
            hashmap[e].append(c)
            hashmap[c].append(e)
        print(hashmap)

        def dfs(cur):
            for nei in hashmap[cur]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for cur in range(n):
            if not visit[cur]:
                visit[cur] = True
                dfs(cur)
                res += 1
        return res
