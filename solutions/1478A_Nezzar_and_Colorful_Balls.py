a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    l=0
    r=0
    Max=0
    while r<len(arr):
        if arr[r]==arr[l]:
            Max=max(Max,r+1-l)
            r+=1
        else:
            l=r
    print(Max)
 
 