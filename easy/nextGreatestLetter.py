from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 2

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        l = 0
        r = len(letters) - 1
        while l <= r:
            p = (l + r) // 2

            if target >= letters[p]:
                # > in usual bs
                l = p + 1

            if target < letters[p]:
                r = p - 1

        return letters[l]
