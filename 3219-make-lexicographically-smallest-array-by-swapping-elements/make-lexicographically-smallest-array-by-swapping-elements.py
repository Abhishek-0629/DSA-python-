class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = nums[:]

        i = 0

        while i < n:
            j = i

            # Find one group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Original indices of this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Values are already sorted
            for k in range(j - i + 1):
                ans[indices[k]] = arr[i + k][0]

            i = j + 1

        return ans
