class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        f, s = 1, 2

        for _ in range(2, n):
            f, s = s, f + s

        return s
