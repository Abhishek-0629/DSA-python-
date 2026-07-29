class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {}
        for i in range(n):
            r = target-nums[i]
            if r in h:
                return [h[r],i]
            h[nums[i]]=i
       # for i in range(0,n):
        #    for j in range(i+1,n):
           #     if nums[i] + nums[j] == target:
                  #  return [i,j]

