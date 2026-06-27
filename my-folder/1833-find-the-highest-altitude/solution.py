class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        highestPoint = cur

        for altGain in gain:
            cur += altGain

            highestPoint = max(cur, highestPoint)

        return highestPoint
