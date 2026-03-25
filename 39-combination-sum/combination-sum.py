class Solution:
    def sol(self, c, t, res, start, current_sum):
        if current_sum == t:
            self.op.append(list(res))
            return

        for i in range(start, len(c)):
            if current_sum + c[i] <= t:
                res.append(c[i])
                self.sol(c, t, res, i, current_sum + c[i])
                res.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.op = [] 
        self.sol(candidates, target, [], 0, 0)
        return self.op
