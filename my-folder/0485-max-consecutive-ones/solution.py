class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax = 0
        totalMax = 0

        for n in nums:
            if n == 1:
                curMax += 1
                totalMax = max(curMax, totalMax)
            else:
                curMax = 0
        
        return totalMax
        
