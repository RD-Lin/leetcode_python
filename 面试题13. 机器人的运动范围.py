#规律递推，每个点检查左边和上边
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dsum(x):
            res = 0
            while x:
                res += x%10
                x = x//10
            return res
        
        flag = [[False]*n for _ in range(m)]
        flag[0][0] = True
        res = 0
        for i in range(m):
            for j in range(n):
                if dsum(i) + dsum(j) <= k and (flag[max(0, i-1)][j] or flag[i][max(j-1, 0)]):
                    flag[i][j] = True
                    res += 1
        return res
        
# bfs, 可以减少扫描次数        
from collections import deque
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dsum(x):
            res = 0
            while x:
                res += x%10
                x = x//10
            return res

        que = deque([(0, 0)])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        res = 1
        while que:
            x, y = que.popleft()
            for nx, ny in [(x, y+1), (x+1, y)]:
                if nx<m and ny<n and not visited[nx][ny] and dsum(nx)+dsum(ny)<=k:
                    visited[nx][ny] = True
                    res += 1
                    que.append((nx, ny))
        return res
        
# dfs
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dsum(x):
            res = 0
            while x:
                res += x%10
                x = x//10
            return res
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        res = 1

        def dfs(x, y):
            nonlocal res
            for nx, ny in [(x, y+1), (x+1, y)]:
                if nx<m and ny<n and not visited[nx][ny] and dsum(nx)+dsum(ny)<=k:
                    visited[nx][ny] = True
                    res += 1
                    dfs(nx, ny)
        dfs(0, 0)
        return res
