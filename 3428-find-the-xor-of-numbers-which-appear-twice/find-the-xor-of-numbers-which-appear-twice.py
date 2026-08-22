class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        a = 0 
        for i in set(nums):
            if nums.count(i)==2:
                a^=i
        return a
