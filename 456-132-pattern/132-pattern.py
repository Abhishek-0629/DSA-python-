class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        stack =[]
        second =  float('-inf')
        for i in range(n-1,-1,-1):
            if nums[i]<second:
                return True 
            while stack and stack[-1]<nums[i]:
                second=stack.pop()
            stack.append(nums[i])
        return False 
     #   n=len(nums)
      #  for i in range(n):
      #      for j in range(i+1,n):
              #  for k in range(j+1,n):
                   # if nums[i]<nums[k]<nums[j]:
                       # return True 
     #   return False 