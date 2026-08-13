class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        m=nums[-1]*nums[-2]
        n=nums[0]*nums[1]
        return m-n
        