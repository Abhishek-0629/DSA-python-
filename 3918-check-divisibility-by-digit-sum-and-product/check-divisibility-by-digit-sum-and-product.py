class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n 
        sum1=0
        product=1
        while num>0:
            last=num%10
            sum1+=last
            product*=last
            num=num//10
            divisor=sum1+product
        return n%divisor==0

       