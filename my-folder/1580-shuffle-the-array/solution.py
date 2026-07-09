class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        left = nums[:n]
        right = nums[n:]
        res = []
        for i in range(n):
            res.append(left[i])
            res.append(right[i])

        return res
