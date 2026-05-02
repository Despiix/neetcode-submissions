class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdig = set() # r + c
        negdig = set() # r - c

        res = []
        board = [["."] * n for i in range(n)]

        def dfs(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (i + c) in posdig or (i - c) in negdig:
                    continue
                
                col.add(c)
                posdig.add(i + c)
                negdig.add(i - c)
                board[i][c] = "Q"

                dfs(i + 1)

                col.remove(c)
                posdig.remove(i + c)
                negdig.remove(i - c)
                board[i][c] = "."
        
        dfs(0)
        return res
