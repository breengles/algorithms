from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = list(sorted(nums))
        l = 0
        r = len(nums) - 1

        while l < r:
            if tmp[l] + tmp[r] < target:
                l += 1
            if tmp[l] + tmp[r] > target:
                r -= 1
            if tmp[l] + tmp[r] == target:
                break

        out = []
        for idx, val in enumerate(nums):
            if val in (tmp[l], tmp[r]):
                out.append(idx)

        return out

