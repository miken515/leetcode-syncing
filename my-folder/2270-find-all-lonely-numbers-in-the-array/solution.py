class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []

        for num, count in freq.items():
            if count == 1 and num - 1 not in freq and num + 1 not in freq:
                res.append(num)

        return res

            
