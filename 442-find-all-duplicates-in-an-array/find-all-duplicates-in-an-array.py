class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #optimal 
        ans = []
        for num in nums:
            index = abs(num)-1
            if nums[index]<0:
                ans.append(abs(num))
            else:
                nums[index]=-nums[index]
        return ans 










      #  seen=set()
      #  ans = []
       # for num in nums:
        #    if num in seen:        TC=O(n)   and Space =O(n)
              #  ans.append(num)
          #  else:
           #     seen.add(num)
      #  return ans 
