class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**0.5)+1):
            x = c-a*a
            l=0
            r=int(x**0.5)
            while l<=r:
                mid = (l+r)//2
                s=mid*mid
                if s==x:
                    return True 
                elif s<x:
                    l=mid+1
                else:
                    r=mid-1
        return False 