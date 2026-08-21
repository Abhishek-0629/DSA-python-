class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=set(arr)
        ans=0 
        num=1
        while k>0:
            if num not in s:
                k-=1
            if k ==0:
                return num 
            num+=1
       