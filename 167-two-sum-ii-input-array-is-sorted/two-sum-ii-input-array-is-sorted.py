class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left = 0
        right = n-1
        while left<right:
            total=numbers[left]+numbers[right]
            if target==total:
                return [left+1,right+1]
            elif target>total:
                left+=1
            else:
                right-=1
      