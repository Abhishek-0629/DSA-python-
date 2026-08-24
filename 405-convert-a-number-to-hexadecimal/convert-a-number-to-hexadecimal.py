class Solution:
    def toHex(self, num: int) -> str:
        if num ==0:
            return "0"
        char = "0123456789abcdef"
        result = ""

        if num<0:
            num+=2**32
        
        while num>0:
            rem=num%16
            result=char[rem]+result
            num=num//16
        return result 