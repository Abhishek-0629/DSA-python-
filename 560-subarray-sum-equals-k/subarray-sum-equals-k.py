class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        prefix=0
        count=0
        for num in nums:
            prefix=prefix+num
            need=prefix-k

            if need in mp:
                count+=mp[need]
            if prefix in mp:
                mp[prefix]+=1
            else:
                mp[prefix]=1
        return count 
        #n =len(nums)
       # count = 0
       # for i in range(n):
        #    current_sum=0
         #   for j in range(i,n):
              #  current_sum+=nums[j]
               # if current_sum==k:
                 #   count+=1
       # return count 
            