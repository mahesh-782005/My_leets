class Solution:
    def mult(self,n):
        x = 9
        val =1
        for i in range(n-1):
            val = val*x
            x-=1
        return val
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        total = 0
        if(n==0):
            return 1
        if(n>=1):
            total+=10
        while(n>1):
            total = total+9*self.mult(n)
            n-=1
        return total

        