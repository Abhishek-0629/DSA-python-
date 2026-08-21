class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        x=10**5
        return max(nums[0]*nums[1]*x,
        nums[-1]*nums[-2]*x,
        nums[0]*nums[-1]*(-x))