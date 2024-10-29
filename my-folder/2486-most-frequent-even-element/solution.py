class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        val = -1
        d = {}
        for num in nums:
            if num % 2 == 0:
                temp = 1 + d.get(num, 0)
                d[num] = temp
                if temp > count or (temp == count and num < val):
                    count = temp
                    val = num
        return val

