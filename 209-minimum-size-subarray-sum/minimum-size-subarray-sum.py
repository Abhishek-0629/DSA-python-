class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        count=0
        ml = float('inf')
        for r in range (n):
            count+= nums[r]
            while count>=target:
                ml = min(ml,r-low+1)
                count-=nums[low]
                low+=1
        return 0 if ml == float('inf') else ml

       
