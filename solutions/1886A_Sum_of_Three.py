import sys
input = sys.stdin.readline
 
def solve():
    n = int(input())
    if n < 7 or n == 9:
        print("NO")
        return
    if n % 3 == 0:
        x, y, z = 1, 4, n - 5
    else:
        x, y, z = 1, 2, n - 3
    print("YES")
    print(x, y, z)
 
t = int(input())
for _ in range(t):
    solve()