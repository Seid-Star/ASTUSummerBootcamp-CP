from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """Count numbers <= x divisible by at least one coin."""
            total = 0

            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            break

                if multiple <= x:
                    if bits % 2:
                        total += x // multiple
                    else:
                        total -= x // multiple

            return total

        # The answer cannot exceed min(coins) * k.
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left