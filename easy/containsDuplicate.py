from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        in_list = set()
        for num in nums:
            if num in in_list:
                return True
            in_list.add(num)

        return False
