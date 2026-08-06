class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            Temp=n
            Product=1
            while Temp>0:
                digits=Temp%10
                Product*=digits 
                Temp//=10
            if Product%t==0:
                return n
            n+=1
        