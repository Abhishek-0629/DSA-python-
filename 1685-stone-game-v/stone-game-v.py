from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(i, j):
            if i >= j:
                return 0

            ans = 0
            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Even the maximum possible contribution
                    # cannot beat ans
                    if ans >= 2 * left:
                        continue

                    ans = max(ans, left + dfs(i, k))

                elif left > right:
                    # As k increases, right only gets smaller.
                    # If this cannot improve ans, later splits
                    # cannot improve it either.
                    if ans >= 2 * right:
                        break

                    ans = max(ans, right + dfs(k + 1, j))

                else:
                    ans = max(
                        ans,
                        left + dfs(i, k),
                        right + dfs(k + 1, j)
                    )

            return ans

        return dfs(0, n - 1)