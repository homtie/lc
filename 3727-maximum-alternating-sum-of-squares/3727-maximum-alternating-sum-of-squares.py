
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted((x * x for x in nums), reverse=True)

        n = len(nums)
        return sum(nums[:(n + 1) // 2]) - sum(nums[(n + 1) // 2:])

