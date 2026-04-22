from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        perimeter = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    q = deque([(i, j)])
                    seen.add((i, j))

                    while q:
                        x, y = q.popleft()

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            # case 1: out of bounds → edge
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                perimeter += 1
                            # case 2: water → edge
                            elif grid[nx][ny] == 0:
                                perimeter += 1
                            # case 3: land → continue BFS
                            elif (nx, ny) not in seen:
                                seen.add((nx, ny))
                                q.append((nx, ny))

        return perimeter