class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}  #存储访问过的元素
        for i, val in enumerate(nums):
            if target-val in visited:
                return [i, visited[target-val]]
            visited[val] = i
        
