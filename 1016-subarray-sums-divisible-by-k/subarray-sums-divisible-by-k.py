class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        prefix=0
        mp={0:1}
        for num in nums:
            prefix=prefix+num
            rem=prefix%k
            if rem<0:
                rem=rem+k
            if rem in mp:
                count+=mp[rem]
                mp[rem]+=1
            else:
                mp[rem]=1
        return count 