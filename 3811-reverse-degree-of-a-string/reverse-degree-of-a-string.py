class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        idx=1
        for ch in s:
            ans+=(123-ord(ch))*idx
            idx+=1
        return ans 