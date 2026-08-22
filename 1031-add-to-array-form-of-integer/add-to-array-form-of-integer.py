class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=0
        for digit in num:
            n=n*10+digit
        n+=k
        ans=[]
        while n>0:
            last_digit=n%10
            ans.append(last_digit)
            n//=10
        return ans[::-1]