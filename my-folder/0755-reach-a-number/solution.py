class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        res = 0

        while target > 0:
            res += 1
            target -= res

        return res if target % 2 == 0 else res + 1 + res % 2
