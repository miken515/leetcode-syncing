class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri = []

        for rowNum in range(numRows):
            row = [None for i in range(rowNum + 1)]

            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = tri[rowNum - 1][j - 1] + tri[rowNum - 1][j]

            tri.append(row)
        
        return tri
