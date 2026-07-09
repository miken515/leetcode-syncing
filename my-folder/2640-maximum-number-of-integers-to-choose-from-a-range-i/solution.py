class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        bannedSet = set(banned)
        count = 0

        for num in range(1, n + 1):
            if num in bannedSet:
                continue
            
            if maxSum - num < 0:
                return count
            
            maxSum -= num
            count += 1
        
        return count
