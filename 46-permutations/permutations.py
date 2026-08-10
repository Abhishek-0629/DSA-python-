class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(subset):
            if len(subset)==len(nums):
                result.append(subset.copy())
                return 
            for num in nums:
                if num not in  subset:
                    subset.append(num)
                    solve(subset)
                    subset.pop()
        solve([])
        return result                   
        
        