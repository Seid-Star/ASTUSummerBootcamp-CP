class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter < x1:
            x = x1
        elif xCenter > x2:
            x = x2
        else:
            x = xCenter

        if yCenter < y1:
            y = y1
        elif yCenter > y2:
            y = y2
        else:
            y = yCenter

        dx = xCenter - x
        dy = yCenter - y

        if dx * dx + dy * dy <= radius * radius:
            return True

        return False