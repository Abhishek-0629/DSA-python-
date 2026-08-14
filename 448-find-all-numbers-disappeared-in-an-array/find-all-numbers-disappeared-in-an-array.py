class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set(nums)
        ans =[]
        for i in range(1,n+1):
            if i not in seen:
                ans.append(i)
        return ans 