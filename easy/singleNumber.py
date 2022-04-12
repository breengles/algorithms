from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num  # xor: x^x = 0 only single (without pair) number will survive

        return res

