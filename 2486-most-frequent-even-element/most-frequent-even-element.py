class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            if num%2==0:
                if num in count:
                    count[num]+=1
                else:
                    count[num]=1
        ans =-1
        max_count=0
        for num in count:
            if count[num]>max_count:
                max_count=count[num]
                ans=num
            elif count[num]==max_count and num<ans:
                ans=num
        return ans 