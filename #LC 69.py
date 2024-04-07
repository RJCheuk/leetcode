#LC 69.py
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, -1 #ans=0是为了防止x=0的情况
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans