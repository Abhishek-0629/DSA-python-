class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        
        cnt = [0] * 26
        
        for ch in s:
            cnt[ord(ch) - 97] += 1
        
        mid = ""
        freq = [0] * 26
        
        for i in range(26):
            if cnt[i] % 2:
                mid = chr(i + 97)
            freq[i] = cnt[i] // 2
        
        n = sum(freq)

        # factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i

        # initial permutation count
        total = fact[n]
        for x in freq:
            total //= fact[x]

        if k > total:
            return ""

        ans = []

        for pos in range(n):
            remaining = n - pos

            for ch in range(26):
                if freq[ch] == 0:
                    continue

                # number of permutations if we put ch here
                ways = total * freq[ch] // remaining

                if k > ways:
                    k -= ways
                else:
                    ans.append(chr(ch + 97))

                    # update count after fixing this character
                    total = ways
                    freq[ch] -= 1
                    break

        left = ''.join(ans)

        return left + mid + left[::-1]