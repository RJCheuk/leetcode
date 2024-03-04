#LC 344.py 反转字符
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 一左一右两个指针相向而行
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right -1