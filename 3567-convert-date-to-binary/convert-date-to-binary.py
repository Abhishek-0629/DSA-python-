class Solution:
    def convertDateToBinary(self, date: str) -> str:
       year,month,day=date.split("-")
       year=int(year)
       month=int(month)
       day=int(day)
       return bin(year)[2:] + "-" +bin(month)[2:]+"-"+bin(day)[2:]

    