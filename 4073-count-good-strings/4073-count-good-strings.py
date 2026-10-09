
class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7

        def fib(k):
            if k == 0:
                return (0, 1)

            a, b = fib(k // 2)
            c = a * (2 * b - a) % MOD
            d = (a * a + b * b) % MOD

            if k % 2:
                return (d, (c + d) % MOD)
            return (c, d)

        return 2 * fib(n)[0] % MOD
