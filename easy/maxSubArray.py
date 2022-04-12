from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i] is the max sum of 0:i subarray that must contain i-th elem
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i]

            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]

            res = max(res, dp[i])

        return res
