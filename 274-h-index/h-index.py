class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n=len(citations)
        H_index=0
        for i in range(n):
            if citations[i]>=i+1:
                H_index+=1
            else:
                break
        return H_index 

