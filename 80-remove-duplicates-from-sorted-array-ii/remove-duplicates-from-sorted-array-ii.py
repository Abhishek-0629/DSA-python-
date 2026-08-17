class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return n 
        i =1
        k = 2
        j = 2
        while(j<n):
             if nums[j] == nums[i-1] and nums[j] == nums[i]: 
                j+=1
                continue 
             else:
                nums[i+1]=nums[j]
                i+=1 
                j+=1 
                k+=1
        return k
        
