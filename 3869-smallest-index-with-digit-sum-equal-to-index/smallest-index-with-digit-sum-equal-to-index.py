class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
       
        for i in range(n):
            x=nums[i]
            total = 0 
            while x>0:
                total+=x%10
                x//=10
            if total ==i:
                return i
        return -1 