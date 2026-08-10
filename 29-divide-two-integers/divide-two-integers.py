class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # Overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Answer ka sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Positive values mein convert
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Divisor ko 2x, 4x, 8x... karte jao
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Largest possible chunk subtract karo
            dividend -= temp
            quotient += multiple

        # Sign apply karo
        if negative:
            quotient = -quotient

        return quotient