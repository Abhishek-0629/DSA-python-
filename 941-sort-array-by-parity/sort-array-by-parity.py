class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        right = 0 
        for left in range(n):
            if nums[left]%2==0:
                nums[left],nums[right]=nums[right],nums[left]
                right+=1
        return  nums 
