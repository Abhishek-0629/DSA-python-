class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        maxi_length=0
        count=defaultdict(int)
        left = 0
        for right in range(n):
            count[nums[right]]+=1
            while count[nums[right]]>k:
                count[nums[left]]-=1
                left+=1
            maxi_length=max(maxi_length ,right-left+1)
        return maxi_length
            