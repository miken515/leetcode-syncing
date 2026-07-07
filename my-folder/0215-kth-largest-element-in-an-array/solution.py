class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minVal = min(nums)
        maxVal = max(nums)
        count = [0] * (maxVal - minVal + 1)

        for n in nums:
            count[n - minVal] += 1
        
        for i in range(len(count) - 1, -1, -1):
            k -= count[i]
            if k <= 0:
                return i + minVal
        
        return -1
