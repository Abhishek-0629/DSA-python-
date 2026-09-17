class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        L=[]
        n=len(nums)
        for i in range(n-1):
            S=nums[i]+nums[i+1]
            if S in L:
                return True 
            else:
                L.append(S)
        return False 