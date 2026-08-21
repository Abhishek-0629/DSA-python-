class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc= True 
        dec=True 
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                inc= False 
                

            if nums[i]<nums[i-1]:
                dec =False 
        return inc or dec 
     