class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left = 0
        total =0
        ans = 0 
        my_dict={}
        right= 0
        while right<n:
            my_dict[nums[right]]=my_dict.get(nums[right],0)+1
            total+=nums[right]

            if right-left+1>k:
                my_dict[nums[left]]-=1
                total-=nums[left]

                if my_dict[nums[left]]==0:
                    del  my_dict[nums[left]]

                left+=1


            if right-left+1==k and len(my_dict)==k:
                ans =max(ans,total)
            right+=1
        return ans 
     