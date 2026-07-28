class Solution:
    def lengthOfLongestSubstring(self, s: str):
        my_dict = {}
        l = 0
        r = 0
        maxi = 0
        n = len(s)

        while r < n:
            if s[r] in my_dict:
                l = max(l, my_dict[s[r]] + 1)

            maxi = max(maxi, r - l + 1)
            my_dict[s[r]] = r
            r += 1

        return maxi