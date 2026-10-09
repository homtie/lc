
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        plus = float('-inf')
        minus = float('-inf')
        del_plus = float('-inf')
        del_minus = float('-inf')
        gap_plus = float('-inf')
        gap_minus = float('-inf')
        ans = float('-inf')

        for x in nums:
            p = max(x, minus + x)
            m = plus - x

            dp = max(del_minus + x, gap_minus + x)
            dm = max(del_plus - x, gap_plus - x)

            gp = plus
            gm = minus

            plus, minus = p, m
            del_plus, del_minus = dp, dm
            gap_plus, gap_minus = gp, gm

            ans = max(ans, plus, minus, del_plus, del_minus)

        return ans
