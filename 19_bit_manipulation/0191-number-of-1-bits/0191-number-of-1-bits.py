class Solution:
    def hammingWeight(self, n: int) -> int:
        b = format(n, 'b')
        return str(b).count('1')