from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """Number of valid amounts <= x."""
            total = 0
            n = len(coins)

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                L = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        if L > x:
                            break
                else:
                    if bits % 2:
                        total += x // L
                    else:
                        total -= x // L

            return total

        # Binary search for the smallest x
        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
