class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = [False] * len(isConnected)

        def dfs(node):
            visited[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visited[i]:
                    dfs(i)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                res += 1
                dfs(i)
        return res
