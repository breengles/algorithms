from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        row = []

        if len(original) != m * n:
            return []

        for idx, item in enumerate(original):
            # idx = j * n + i where j in [0..m], i in [0..n]
            row.append(item)
            if (idx + 1) % n == 0:
                out.append(row)
                row = []

        return out
