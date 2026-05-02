class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []

        atl, pas = set(), set()
        
        def dfs(r, c, ocean, prevh):
            if (r < 0 or c < 0 or r == rows or c == cols or
            (r, c) in ocean or heights[r][c] < prevh ):
                return 
            
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])


        for c in range(cols):
            dfs(0, c, pas, heights[0][c])
            dfs(rows - 1, c , atl, heights[rows- 1][c])
        for r in range(rows):
            dfs(r, 0, pas, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols -1 ])

        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pas and (r,c) in atl:
                    res.append([r, c])
        return res