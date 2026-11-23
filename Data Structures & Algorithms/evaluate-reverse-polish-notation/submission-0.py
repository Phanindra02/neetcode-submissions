class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in tokens:
            if i in ['+','-','*','/']:
                n1,n2=int(stack.pop()),int(stack.pop())
                if i=='+':
                    stack.append(n2+n1)
                elif i=='-':
                    stack.append(n2-n1)
                elif i=='*':
                    stack.append(n2*n1)
                else:
                    stack.append(n2/n1)
            else:
                stack.append(i)
        return int(stack[-1])