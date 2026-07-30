class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        keys = 8
        base = n // keys
        extra = n % keys
        total = 0
        for i in range(keys):
            size = base + (1 if i < extra else 0)
            total += size * (size + 1) // 2
        return total