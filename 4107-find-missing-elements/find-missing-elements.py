class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        mn = min(nums)
        mx=max(nums)
        for x in range(mn+1,mx):
            if x not in nums:
                ans.append(x)
        return ans 
