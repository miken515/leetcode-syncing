class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxOnes = 0
        maxRow = 0

        for i in range(len(mat)):
            curMax = sum(mat[i])

            if curMax > maxOnes:
                maxOnes = curMax
                maxRow = i

        return [maxRow, maxOnes]
