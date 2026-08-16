class Solution:
    def mySqrt(self, x: int) -> int:
        if x<0:
            return x
        left = 1
        right=x
        while left<=right:
            mid=(left+right)//2
            S=mid*mid
            if S==x:
                return mid 
            elif S<x:
                left=mid+1
            else:
                right=mid-1
        return right 
        