class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i =0
        s = ""
        n = len(strs)
        while(i< len(min(strs))):
            f =0
            c = strs[0][i]
            for j in range(n):
                if strs[j][i] !=c:
                    f=1
                    break
            if f ==1:
                break
            else:
                s+=c
            i+=1
        return s
