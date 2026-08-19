class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] = rows.get(row, 0) | (1 << seat)

        # Rows without any relevant reservation can fit 2 groups
        ans = 2 * (n - len(rows))

        for mask in rows.values():
            left = (mask & (1 << 2 | 1 << 3 | 1 << 4 | 1 << 5)) == 0
            middle = (mask & (1 << 4 | 1 << 5 | 1 << 6 | 1 << 7)) == 0
            right = (mask & (1 << 6 | 1 << 7 | 1 << 8 | 1 << 9)) == 0

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans