class Solution:
    def gen(self,res, o, c , bal, curr):
        
        if(o==0 and c==0 and bal ==0):
            res.append(curr)
            return
        
        if(bal >=0 and o!=0):
            self.gen(res, o-1,c,bal+1,curr+"(")
        
        if(bal>0 and c!=0):
            self.gen(res, o,c-1,bal-1,curr+")")
        return
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        bal = 0
        o = n
        c = n
        self.gen(res, o,c,bal,"")
        print(res)
        res = list(set(res))
        return res