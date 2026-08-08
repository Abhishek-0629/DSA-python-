class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total_sum=0
        temp=x
        while x>0:
            last_digit=x%10
            total_sum=total_sum+last_digit
            x//=10
        if temp%total_sum==0:
            return total_sum
        else:
            return -1 
               
        