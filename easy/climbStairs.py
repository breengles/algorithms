class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        nums = [0] * n

        nums[0] = 1
        nums[1] = 2

        for i in range(2, len(nums)):
            nums[i] = nums[i - 2] + nums[i - 1]

        return nums[-1]
