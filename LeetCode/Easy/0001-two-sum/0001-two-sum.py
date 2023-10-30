class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, n in enumerate(nums):
            numbers[n] = i

        for i, n in enumerate(nums):
            if target - n in numbers and i != numbers[target - n]:
                return nums.index(n), numbers[target - n]