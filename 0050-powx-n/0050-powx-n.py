
import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if x == 1.0:
            return 1.0

        if x == -1.0:
            return -1.0 if n % 2 else 1.0

        if x == 0.0:
            return 0.0

        # Stabilize calculations when |x| is close to 1
        if abs(abs(x) - 1.0) < 1e-7:
            exponent = n * math.log(abs(x))
            result = math.exp(exponent)
            if x < 0 and n % 2 != 0:
                result = -result
            return result

        if n < 0:
            x = 1.0 / x
            n = -n

        result = 1.0

        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2

        return result
