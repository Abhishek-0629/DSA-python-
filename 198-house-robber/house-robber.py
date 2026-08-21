class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=0
        prev1=0
        for money in nums:
            current=max(prev,money+prev1)
            prev1=prev
            prev=current
        return prev
