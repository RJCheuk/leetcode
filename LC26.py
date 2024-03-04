#LC26.py 快慢指针原地修改数组
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        slow=0
        fast=1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow]= nums[fast]
            fast += 1
        return slow + 1