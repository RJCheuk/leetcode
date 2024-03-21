#LC 303 区域和检索-数组不变
class NumArray:

    def __init__(self, nums: List[int]):
        # 前缀和数组
        self.preSum = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]


    def sumRange(self, left: int, right: int) -> int:
         # 查询闭区间 [left, right] 的累加和
        return self.preSum[right + 1] - self.preSum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)