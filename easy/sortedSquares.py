from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [num ** 2 for num in nums]  # O(n)
        if nums[-1] <= 0:
            return [num ** 2 for num in reversed(nums)]  # O(n)

        negs = []
        out = []
        for idx, num in enumerate(nums):  # O(n)
            if num < 0:
                negs.append(num ** 2)
            if num >= 0:
                break

        neg_idx = len(negs) - 1
        while neg_idx > -1 and idx < len(nums):  # O(n)
            x = nums[idx] ** 2
            y = negs[neg_idx]
            if x < y:
                out.append(x)
                idx += 1
            elif x == y:
                out.append(x)
                out.append(y)
                idx += 1
                neg_idx -= 1
            else:
                out.append(y)
                neg_idx -= 1

        if idx < len(nums):
            out.extend([num ** 2 for num in nums[idx:]])
        if neg_idx > -1:
            out.extend([num for num in reversed(negs[: neg_idx + 1])])

        return out
