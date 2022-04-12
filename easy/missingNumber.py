from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target_sum = n * (n + 1) // 2  # simple partial sum from 1 to n
        real_sum = sum(nums)
        return target_sum - real_sum
