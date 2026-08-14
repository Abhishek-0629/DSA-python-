class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans=0
        n=len(s)
        count=defaultdict(int)
        for right in range(n):
            count[s[right]]+=1
            while count[s[right]]>2:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
