class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0
        last = [0] * 26
        for ch in s:
            i = ord(ch) - ord('a')
            new_dp = (2 * dp + 1 - last[i]) % MOD
            last[i] = dp + 1
            dp = new_dp
        return dp
