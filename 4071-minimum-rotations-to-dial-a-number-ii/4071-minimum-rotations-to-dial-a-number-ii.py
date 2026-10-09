
class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dist(a, b):
            diff = abs(int(a) - int(b))
            return min(diff, 10 - diff)

        ans = dist('0', s[0])

        for i in range(1, n):
            ans += dist(s[i - 1], s[i])

        best = ans

        for k in range(n):
            if k == 0:
                old = dist('0', s[0])
                new = dist('0', s[n - 1])
            else:
                old = dist(s[k - 1], s[k])
                new = dist(s[k - 1], s[n - 1])

            best = min(best, ans - old + new)

        return best
