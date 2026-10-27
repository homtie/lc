
from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        grid = [["#"] * n for _ in range(m)]

        # Make the entire first row free.
        grid[0] = ["."] * n

        # Make the last column free.
        for i in range(m):
            grid[i][n - 1] = "."

        return ["".join(row) for row in grid]
