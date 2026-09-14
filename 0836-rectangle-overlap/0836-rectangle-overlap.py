class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a = min(rec2[0], rec2[2])
        b = max(rec1[0], rec1[2])
        c = min(rec1[0], rec1[2])
        d = max(rec2[0], rec2[2])

        e = min(rec2[1], rec2[3])
        f = max(rec1[1], rec1[3])
        g = min(rec1[1], rec1[3])
        h = max(rec2[1], rec2[3])

        if a < b and c < d and e < f and g < h:
            return True
        else:
            return False
