class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        firstEdge = edges[0]
        secondEdge = edges[1]

        return firstEdge[0] if firstEdge[0] in secondEdge else firstEdge[1]


