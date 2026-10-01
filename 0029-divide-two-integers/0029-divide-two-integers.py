class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:

            current = divisor
            count = 1

            # Double until it becomes too large
            while dividend >= current + current:
                current += current
                count += count

            dividend -= current
            result += count

        return -result if negative else result