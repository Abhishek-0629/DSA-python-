class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n):
            product=nums[n-1]*nums[n-2]*nums[n-3]
            product1=nums[0]*nums[1]*nums[n-1]
        return max(product,product1)
     
