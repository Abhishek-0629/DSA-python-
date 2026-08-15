class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n=len(s)
        m=len(goal)
        if n!=m:
            return False 
        d = s + s
        if goal in d:
            return True 
        else:
            return False 
          
      