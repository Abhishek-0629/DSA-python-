class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        m=len(goal)
        if n!=m:
            return False 
        d = s + s
        return goal in d 
          
      