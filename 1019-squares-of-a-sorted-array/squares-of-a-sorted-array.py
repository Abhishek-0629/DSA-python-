class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        ans=[0]*n
        index=n-1
        while left<=right:
            Leftsquare=nums[left]*nums[left]
            Rightsquare=nums[right]*nums[right]
            if Leftsquare>Rightsquare:
                ans[index]=Leftsquare
                left+=1
            else:
                ans[index]=Rightsquare
                right-=1
            index-=1
        return ans 

        #result=[]
        #for i in range(len(nums)):
         #   result.append(nums[i]*nums[i])
       # result.sort()
       # return result 
       