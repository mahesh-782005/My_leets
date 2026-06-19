class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        top =-1
        n = len(s)
        i =0
        res = ""
        start = 1
        while(i<n):
            if s[i] == "(":
                stack.append("(")
                top+=1
            else:
                stack.pop()
                top-=1
            if top == -1 and i>0:
                res+= s[start:i]
                start= i+2
            i+=1            
        return res

