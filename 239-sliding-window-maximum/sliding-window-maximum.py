from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        ans =[]
        n=len(nums)
        for i in range(n):
            if  dq and dq[0]<=i-k:#Revome indices outside the current window 
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:#Remove smaller elements from the back 
                dq.pop()
            dq.append(i)#starting adding answers once the first window is formed 

            if i>=k-1:
                ans.append(nums[dq[0]])#In dedue front elements always maximum 
        return ans 

       # n=len(nums)
       # ans =[]
       # for i in range(n-k+1):
          #  for j in range(i,i+k):
              #  if nums[j]>nums[i]:
                #    nums[i]=nums[j]
           # ans.append(nums[i])
       # return ans 