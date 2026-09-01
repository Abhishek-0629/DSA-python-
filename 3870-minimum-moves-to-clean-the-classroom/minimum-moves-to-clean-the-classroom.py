from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Find start and assign an index to every litter.
        sr = sc = 0
        litter_id = {}
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        # No litter to collect.
        if k == 0:
            return 0

        target = (1 << k) - 1

        # State = (row, col, remaining_energy, mask)
        q = deque([(sr, sc, energy, 0)])
        visited = {(sr, sc, energy, 0)}

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                # All litter collected.
                if mask == target:
                    return moves

                # Cannot make another move.
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # One move costs one energy.
                    ne = e - 1
                    nmask = mask

                    # Reset energy.
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # Collect litter.
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        nmask |= 1 << idx

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1
