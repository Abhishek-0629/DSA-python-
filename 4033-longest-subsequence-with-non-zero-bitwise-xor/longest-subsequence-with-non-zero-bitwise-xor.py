class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        count_zero=0
        for  x in nums:
            ans^=x

            if x==0:
                count_zero+=1
        if  ans !=0:
            return n 
        if count_zero==n:
            return 0 
        return n-1 
        