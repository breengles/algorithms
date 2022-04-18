from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cand = None

        for num in nums:
            if cnt == 0:
                cand = num

            if num == cand:
                cnt += 1
            else:
                cnt -= 1

        return cand

