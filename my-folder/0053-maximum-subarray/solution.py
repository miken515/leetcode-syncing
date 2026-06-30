class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadanes Algo
        curSub = nums[0]
        maxSub = nums[0]

        for num in nums[1:]:
            curSub = max(num, curSub + num)
            maxSub = max(maxSub, curSub)

        return maxSub
