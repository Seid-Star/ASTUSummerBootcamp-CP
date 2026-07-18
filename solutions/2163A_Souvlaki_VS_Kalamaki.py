t = int(input())
 
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
 
    ok = True
    for i in range(n - 1):
        if i % 2 != 0:
            if a[i] > a[i + 1] or a[i]<a[i+1]:
                ok = False
    print("YES" if ok else "NO")