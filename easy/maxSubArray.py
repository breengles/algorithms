from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i]

            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]

            res = max(res, dp[i])

        return res
