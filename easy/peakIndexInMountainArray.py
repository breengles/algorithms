from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 1  # peak could not be at the beginning
        r = len(arr) - 2  # -//- at the end

        while l <= r:
            p = (l + r) // 2

            if arr[p - 1] < arr[p] > arr[p + 1]:  # peak condition
                return p

            if arr[p - 1] < arr[p]:  # always climb up
                l = p + 1
            else:
                r = p - 1

