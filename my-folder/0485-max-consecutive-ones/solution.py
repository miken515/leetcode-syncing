class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                maxOne = max(maxOne, count)
                count = 0
        
        return max(maxOne, count)
