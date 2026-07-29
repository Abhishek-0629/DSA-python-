class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n =len(nums)
        x = 0
        for i in range(n):
            if nums[i]!=val:
                nums[x]=nums[i]
                x+=1
        return x 
    