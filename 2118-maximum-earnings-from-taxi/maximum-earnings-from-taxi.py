class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda r: r[0])  # sort by start time
        m = len(rides)
        dp = [-1] * (m + 1)  # dp[i] = best profit using rides[i:]

        def find_next(end_time):
            # find first index j such that rides[j][0] >= end_time
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) // 2
                if rides[mid][0] >= end_time:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def rec(i):
            if i == m:
                return 0
            if dp[i] != -1:
                return dp[i]

            # option 1: skip ride i
            skip = rec(i + 1)

            # option 2: take ride i, jump to next non-overlapping ride
            start, end, tip = rides[i]
            profit = end - start + tip
            j = find_next(end)
            take = profit + rec(j)

            dp[i] = max(skip, take)
            return dp[i]

        return rec(0)