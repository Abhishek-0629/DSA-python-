class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        ans =nums[0]
        nameset=set(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]+1:
                break 
            ans+=nums[i]
        while ans in nameset:
            ans+=1
        return ans 

        
        