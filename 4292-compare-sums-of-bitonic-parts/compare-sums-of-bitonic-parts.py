class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        peak=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[i+1]:
                peak=i
                break
        leftsum=0
        rightsum=0
        for i in range(peak+1):
            leftsum+=nums[i]
        for i in range(peak,n):
            rightsum+=nums[i]
        if leftsum>rightsum:
            return 0 
        elif leftsum<rightsum:
            return 1
        else:
            return -1 
        