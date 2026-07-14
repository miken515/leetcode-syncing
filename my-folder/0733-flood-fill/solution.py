class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        
        clr = image[sr][sc]
        if clr == color:
            return image
        
        def dfs(r, c):
            if image[r][c] == clr:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < ROWS:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < COLS:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image

