class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ans=[]
        m=max(candies)
        for i in range(n):
            if candies[i]+extraCandies>=m:
                ans.append(True)
               
                i+=1
            else:
                ans.append(False)
        return ans 
                

        