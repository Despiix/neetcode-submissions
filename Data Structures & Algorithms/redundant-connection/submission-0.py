class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)] # why +1?

        def dfs(node, par):
            if visit[node]:
                return True
           
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)
            visit = [False] * (len(edges) + 1) # When do I use visited with False? (instead of coords)
            # Why is visit in the loop?

            if dfs(p, -1):
                return[p, c]
        return []


            


            
            
                