from math import ceil, sqrt
a=int(input())
for x in range(a):
    k=int(input())
    n=ceil(sqrt(k))
    mx=n*n
    mid=mx-n+1
    if k >= mid:
        print(n, mx - k + 1)
    else:
        print(k - (mx - 2 * n + 1), n)