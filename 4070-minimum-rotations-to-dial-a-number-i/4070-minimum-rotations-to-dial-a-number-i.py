
class Solution:
    def minRotations(self, s: str) -> int:
        ans = 0
        curr = 0

        for ch in s:
            digit = int(ch)
            diff = abs(digit - curr)
            ans += min(diff, 10 - diff)
            curr = digit

        return ans
