class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        st=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in d.values():
                st.append(i)
            elif i in d.keys():
                if len(st)==0:
                    return False
                if st.pop()!=d[i]:
                    return False
        if len(st)==0:
            return True
        return False