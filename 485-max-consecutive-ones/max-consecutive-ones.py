class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        maxi_count=0
        for i in range(n):
            if nums[i]==1:
                count+=1
                maxi_count=max(maxi_count,count)
            else:
                count=0
        return maxi_count
       