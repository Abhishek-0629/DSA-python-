class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for bracket in s:
            if bracket=="(" or bracket=="{" or bracket=="[":
                st.append(bracket)
            else:
                if len(st)==0:
                    return False 
                ch=st.pop()
                if( (bracket==")" and    ch=="(") or (bracket=="}"  and ch=="{") or (bracket=="]"  and ch =="[")):
                    continue 
                else:
                    return False 
        return len(st)==0



