# bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        m, n = len(image), len(image[0])
        oriColor = image[sr][sc]

        def neighbours(i, j):
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == oriColor:
                    yield x, y
        
        stack = [(sr, sc)]
        image[sr][sc] = newColor
        while stack:
            for x, y in neighbours(*stack.pop()):
                image[x][y] = newColor
                stack.append((x, y))
        
        return image
        
        
#dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        m, n = len(image), len(image[0])
        oriColor = image[sr][sc]

        def neighbours(i, j):
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == oriColor:
                    yield x, y

        def dfs(sr, sc):
            image[sr][sc] = newColor
            for x, y in neighbours(sr, sc):
                dfs(x, y)

        dfs(sr, sc)
        
        return image
 
 
#并查集
class Solution:
  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
      if image[sr][sc] == newColor: return image
      m, n = len(image), len(image[0])
      oriColor = image[sr][sc]

      parents = [i for i in range(m*n)]

      #每次查询时尝试压缩路径
      def find(idx):
          while idx != parents[idx]:
              parents[idx] = parents[parents[idx]]
              idx = parents[idx]
          return idx

      for i in range(m):
          for j in range(n):
              if image[i][j] != oriColor:
                  continue
              if i+1 < m and image[i+1][j] == image[i][j]:
                  parents[find((i+1)*n+j)] = find(i*n+j)
              if j+1 < n and image[i][j+1] == image[i][j]:
                  parents[find(i*n+j+1)] = find(i*n+j)

      for idx in range(len(parents)):
          if find(idx) == find(sr*n+sc):
              image[idx//n][idx%n] = newColor

      return image
