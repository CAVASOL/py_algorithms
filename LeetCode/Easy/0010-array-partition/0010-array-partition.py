class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = sorted(nums)
        return sum(n[::2])