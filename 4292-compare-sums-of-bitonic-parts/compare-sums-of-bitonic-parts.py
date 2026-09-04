class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        peak = 0 
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                peak=i
                break
        left = 0
        right = 0
        for i in range(peak+1):
            left+=nums[i]
        for i in range(peak,n):
            right+=nums[i]

        if left>right:
            return 0 
        elif left<right:
            return 1
        else:
            return -1 