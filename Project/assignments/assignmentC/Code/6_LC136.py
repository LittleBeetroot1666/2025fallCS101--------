class Solution:
    def singleNumber(self, nums: [int]) -> int:
        n = 0
        for i in nums:
            n = n ^ i
        return n
