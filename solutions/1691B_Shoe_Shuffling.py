a=int(input())
for x in range(a):
    b=int(input())
    arr=list(map(int,input().split()))
    brr=[0]*len(arr)
    Seid=True
    l=0
    while l<len(arr):
        r=l
        while r<len(arr) and arr[l]==arr[r]:
            r+=1
        if r-l==1:
            Seid=False
            break
        for i in range(l,r-1):
            brr[i]=i+2
        brr[r-1]=l+1
        l=r
    if Seid:
        print(*brr)
    else:
        print(-1)