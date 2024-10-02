class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)

        def dfs(left, right):
            if left > right:
                return 0

            scoreLeft = nums[left] - dfs(left + 1, right)
            scoreRight = nums[right] - dfs(left, right - 1)

            return max(scoreLeft, scoreRight)

        return dfs(0, n - 1) >= 0
