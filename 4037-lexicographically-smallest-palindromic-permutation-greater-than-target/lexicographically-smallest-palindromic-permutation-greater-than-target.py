class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        odd = [i for i in range(26) if cnt[i] % 2]
        if len(odd) > 1:
            return ""

        # Character in the middle (only for odd length)
        mid = chr(ord('a') + odd[0]) if odd else ""

        # Characters available for the left half
        half = [x // 2 for x in cnt]
        m = n // 2

        left = []

        def can_make_greater() -> bool:
            """
            Given the current prefix, construct the largest possible
            palindrome. If it is > target, some valid completion exists.
            """
            prefix = ''.join(left)

            # Largest possible remaining left half
            suffix = []
            for i in range(25, -1, -1):
                if half[i]:
                    suffix.append(chr(ord('a') + i) * half[i])

            left_part = prefix + ''.join(suffix)
            palindrome = left_part + mid + left_part[::-1]

            return palindrome > target

        # Build the left half greedily
        for _ in range(m):
            found = False

            # Try the smallest possible character
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                left.append(chr(ord('a') + c))

                if can_make_greater():
                    found = True
                    break

                # This character cannot lead to an answer
                left.pop()
                half[c] += 1

            if not found:
                return ""

        left = ''.join(left)
        ans = left + mid + left[::-1]

        return ans if ans > target else ""
