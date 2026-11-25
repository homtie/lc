
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        b1, b2 = 100003, 100019
        m1, m2 = 10**9 + 7, 10**9 + 9

        p1 = [0] * (n + 1)
        p2 = [0] * (n + 1)

        for i, x in enumerate(nums):
            p1[i + 1] = (p1[i] * b1 + x) % m1
            p2[i + 1] = (p2[i] * b2 + x) % m2

        def check(k):
            pow1 = pow(b1, k, m1)
            pow2 = pow(b2, k, m2)
            cnt = {}

            for i in range(n - k + 1):
                h1 = (p1[i + k] - p1[i] * pow1) % m1
                h2 = (p2[i + k] - p2[i] * pow2) % m2
                key = (h1, h2)
                cnt[key] = cnt.get(key, 0) + 1

            return any(v == 1 for v in cnt.values())

        lo, hi = 1, n

        while lo < hi:
            mid = (lo + hi) // 2

            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
