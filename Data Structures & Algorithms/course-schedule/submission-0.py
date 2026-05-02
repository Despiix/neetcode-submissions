class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerec = {i:[] for i in range(numCourses)}
        print(prerec)
        for c, p in prerequisites:
            prerec[c].append(p)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prerec[crs] == []:
                return True
            
            visited.add(crs)
            for pre in prerec[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            prerec[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        