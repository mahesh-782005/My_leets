class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        i = 0
        j = 0
        l = [""]*numRows;
        while(i<n):
            for j in range(numRows):
                if i== n:
                    break
                l[j]+= s[i]
                i+=1
            for j in range(numRows-2, 0, -1):
                if i== n:
                    break
                l[j]+= s[i]
                i+=1
        i =0
        res = ""
        while(i<len(l)):
            res+=l[i]
            i+=1
        return res

