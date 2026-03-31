class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        i = 0
        j = len(l)-1
        while(i<j):
            if(l[i] != l[j]):
                return False
            i+=1
            j-=1
        return True
        