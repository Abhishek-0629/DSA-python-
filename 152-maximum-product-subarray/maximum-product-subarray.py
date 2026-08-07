class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        prefix=1
        suffix=1
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-1-i]
            maxi=max(maxi,prefix,suffix)
        return maxi 
       