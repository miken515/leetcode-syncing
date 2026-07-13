class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxMoves = 0
        visited = [[False] * COLS for i in range(ROWS)]
        direction = [1, 0, -1]

        q = deque()
        for i in range(ROWS):
            visited[i][0] = True
            q.append((i, 0, 0))
        
        while q:
            for i in range(len(q)):
                row, col, count = q.popleft()

                maxMoves = max(maxMoves, count)

                for dir in direction:
                    nr, nc = row + dir, col + 1

                    if (
                        0 <= nr < ROWS and
                        0 < nc < COLS and not
                        visited[nr][nc] and
                        grid[row][col] < grid[nr][nc]
                    ):
                        visited[nr][nc] = True
                        q.append((nr, nc, count +  1))
        
        return maxMoves
