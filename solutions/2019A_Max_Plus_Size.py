t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    ans = 0
    for i in range(n):
        if arr[i] == mx:
            count=1+i//2+(n-i-1)//2
            ans=max(ans,mx+count)
    print(ans)