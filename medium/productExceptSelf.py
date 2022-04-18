from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [1] * len(nums)
        suf_prod = [1] * len(nums)

        for idx in range(1, len(nums)):
            pref_prod[idx] = pref_prod[idx - 1] * nums[idx - 1]

        for idx in range(len(nums) - 1, 0, -1):
            suf_prod[idx - 1] = suf_prod[idx] * nums[idx]

        out = []
        for idx in range(len(nums)):
            out.append(pref_prod[idx] * suf_prod[idx])

        return out

