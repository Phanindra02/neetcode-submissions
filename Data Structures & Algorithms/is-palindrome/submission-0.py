class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for i in s:
            if ord('a')<=ord(i.lower())<=ord('z') or ord('0')<=ord(i)<=ord('9'):
                st+=i.lower()
        print(st)
        if st==st[::-1]:
            return True
        return False