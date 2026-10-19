class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        st=[]
        for i in s:
            if i in ['(','[','{']:
                st.append(i)
            elif i in [')',']','}']:
                if len(st)==0:
                    return False
                print(st)
                if i==')':
                    if st.pop()!='(':
                        return False
                elif i==']':
                    if st.pop()!='[':
                        return False
                elif i=='}':
                    if st.pop()!='{':
                        return False
        if len(st)==0:
            return True
        return False