class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + dist)
        for i in range(m - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + dist)
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            dist = id2 - id1
            peak = (h1 + h2 + dist) // 2
            max_height = max(max_height, peak)
        return max_height
