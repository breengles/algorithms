from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self._cumsum(nums)

    def _cumsum(self, nums):
        """
        nums   = [1, 2, 2,  5]
        cumsum = [1, 3, 5, 10]
        """
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]

        for i in range(1, len(nums)):
            self.sums[i] = self.sums[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
