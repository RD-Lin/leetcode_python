#双指针解法
#暴力法-->动态编程(存储双向扫描)-->双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1: return 0
        left, right = 0, n-1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            #巧妙在于每次选取left,right中较小的值，这使得每次只要判断单端max
            if height[left] <= height[right]:
                if left_max >= height[left]:
                    ans +=left_max-height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max >= height[right]:
                    ans += right_max-height[right]
                else:
                    right_max = height[right]
                right -= 1
        return ans
#单调栈，巧妙的地方在于栈内存储索引，每次弹出时储水高度需要乘以距离        
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: return 0
        ans = 0
        stack = []
        cur = 0
        while cur < n:
            while stack and height[stack[-1]] <= height[cur]:
                idx = stack.pop()
                if not stack: break
                distance = cur - stack[-1] - 1
                ans += distance * (min(height[stack[-1]], height[cur])-height[idx])
            stack.append(cur)
            cur += 1
        return ans
