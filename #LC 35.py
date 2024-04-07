#LC 35.py search insert position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #左闭右闭的区间
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right ) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
            
        return right + 1